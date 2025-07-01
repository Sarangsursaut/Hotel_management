from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import OwnerRegisterForm, OwnerLoginForm, HotelForm
from .models import Hotel, HotelBooking
from django.contrib import messages
from django.contrib.auth import get_user_model

User = get_user_model()

def Owner_register(request):
    if request.method == "POST":
        form = OwnerRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.role = 'hotel_owner'  # make sure your CustomUser model has `role`
            user.save()
            messages.success(request, 'Hotel owner registered successfully.')
            return redirect('owner_login')
        else:
            messages.error(request, 'Please fix the form errors.')
    else:
        form = OwnerRegisterForm()
        return render(request, 'hotelapp/owner_register.html', {'form': form})
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
            return redirect('owner_register')

        User.objects.create_user(username=username, password=password, role='hotel_owner')
        messages.success(request, 'Owner registered successfully.')
        return redirect('owner_login')

    return render(request, 'hotelapp/owner_register.html')

def owner_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.role == 'hotel_owner':
                login(request, user)
                return redirect('owner_dashboard')
            else:
                messages.error(request, "Access denied: This is not a hotel owner account.")
        else:
            messages.error(request, "Invalid credentials.")
    return render(request, 'hotelapp/owner_login.html')
   

@login_required(login_url='/hotel/owner/login')
def owner_dashboard(request):
    return render(request, 'hotelapp/owner_dashboard.html')


@login_required(login_url='/hotel/owner/login/')
def submit_hotel(request):
    form = HotelForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            hotel = form.save(commit=False)
            hotel.owner = request.user
            hotel.save()
            messages.success(request, "Hotel submitted successfully.")
            return redirect('owner_my_hotels')
        else:
            messages.error(request, "Please correct the errors below.")
    return render(request, 'hotelapp/submit_hotel.html', {'form': form})

@login_required(login_url='/hotel/owner/login/')
def my_hotels(request):
    hotels = Hotel.objects.filter(owner=request.user).prefetch_related('hotelbooking_set')
    return render(request, 'hotelapp/my_hotels.html', {'hotels': hotels})

def owner_logout(request):
    logout(request)
    return redirect('owner_login')

# Create your views here.

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import get_user_model

user = get_user_model() 
def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        if user.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
            return redirect('register')

        user.objects.create_user(username=username, password=password, role='user')
        messages.success(request, 'User registered successfully.')
        return redirect('login')

    return render(request, 'userapp/register.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.role == 'user':
                login(request, user)
                return redirect('main')
            else:
                messages.error(request, "Access denied: This is not a user account.")
        else:
            messages.error(request, "Invalid credentials.")
    return render(request, 'userapp/login.html')

# Create your views here.

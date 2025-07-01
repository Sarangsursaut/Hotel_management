from django.shortcuts import render,redirect
from hotelapp.models import Hotel
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .models import Booking 

def home(request):
    return render(request, 'booking/main.html')
def main(request):
  hotels = Hotel.objects.filter(is_approved=True)
  return render(request,'booking/home.html',{'hotels': hotels})

@login_required(login_url='login') 
def book_hotel(request, hotel_id):
    if request.method == 'POST':
        Booking.objects.create(user=request.user, hotel=hotel)
        messages.success(request, f"You have booked {hotel.name} successfully!")
        return redirect('hotel_list')
    hotel = get_object_or_404(Hotel, id=hotel_id, is_approved=True)
    return render(request, 'booking/book_hotel.html', {'hotel': hotel})

def hotel_list_view(request):
    hotels = Hotel.objects.filter(is_approved=True)
    return render(request, 'booking/hotel_list.html', {'hotels': hotels})
# Create your views here.


def book_hotel(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id, is_approved=True)

    if request.method == 'POST':
        # Create a simple booking notification entry
        messages.success(request, f"You have booked {hotel.name} successfully!")
        
        # Optional: Save booking to database — you can make a Booking model if needed

        # Set a flag or update something on hotel if needed
        return redirect('hotel_list')  # Redirect to a public page after booking

    return render(request, 'booking/book_hotel.html', {'hotel': hotel})

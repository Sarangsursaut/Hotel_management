from django.contrib import admin
from .models import Room, Booking

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'room_type', 'price', 'is_avaliable']
    list_filter = ['room_type', 'is_avaliable']
    search_fields = ['name']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'user', 'room', 'check_in', 'check_out', 'booked_at']
    list_filter = ['check_in', 'room']
    search_fields = ['customer_name', 'user__username', 'room__name']
    ordering = ['-booked_at']

from django.contrib import admin
from .models import Hotel
from .models import HotelBooking


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'location', 'is_approved']
    list_filter = ['is_approved', 'location']
    search_fields = ['name', 'location']
    list_editable = ['is_approved']
    ordering = ['-id']
    def approve_hotels(self, request, queryset):
        queryset.update(is_approved=True)
    approve_hotels.short_description = "Approve selected hotels"

admin.site.register(HotelBooking)

# Register your models here.

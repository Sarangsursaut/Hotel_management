from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser  # or wherever you defined it

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('User Role', {'fields': ('role',)}),
    )
# Register your models here.

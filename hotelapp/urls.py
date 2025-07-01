from django.urls import path
from . import views


urlpatterns = [
    path('owner/register/',views.Owner_register,name='owner_register'),
    path('owner/dashboard/', views.owner_dashboard, name='owner_dashboard'),
    path('owner/login/', views.owner_login, name='owner_login'),
    path('owner/submit/', views.submit_hotel, name='submit_hotel'),
    path('owner/my-hotels/', views.my_hotels, name='owner_my_hotels'),
    path('owner/logout/', views.owner_logout, name='owner_logout'),
]

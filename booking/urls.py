from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('home/', views.home, name='home'),
    path('hotels/', views.hotel_list_view, name='hotel_list'),
    path('hotels/book/<int:hotel_id>/', views.book_hotel, name='book_hotel'),
]
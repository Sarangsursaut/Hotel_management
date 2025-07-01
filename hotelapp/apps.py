from django.apps import AppConfig

class HotelappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hotelapp'
# from django.db import models
# from django.contrib.auth.models import User

# class Hotel(models.Model):
#   owner=models.ForeignKey(User,on_delete=models.CASCADE)
#   name=models.CharField(max_length=255)
#   location=models.CharField(max_length=255)
#   price_per_night=models.DecimalField(max_digits=8,decimal_places=2)
#   description=models.TextField()
#   image=models.ImageField(upload_to='hote')


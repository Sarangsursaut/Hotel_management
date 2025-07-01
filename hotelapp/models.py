from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Hotel(models.Model):
  owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  name=models.CharField(max_length=100)
  location=models.CharField(max_length=255)
  price_per_night=models.DecimalField(max_digits=8,decimal_places=2)
  description=models.TextField()
  image=models.ImageField(upload_to='hotels/',blank=True,null=True)
  is_approved=models.BooleanField(default=False)

  def __str__(self):
    return self.name

class HotelBooking(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} booked {self.hotel.name}"
# Create your models here.

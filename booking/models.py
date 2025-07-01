from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone 

User = get_user_model()

class Room(models.Model):
  Room_TYPE_CHOICES=[
      ('SINGLE', 'Single'),
      ('DOUBLE', 'Double'),
      ('DELUXE', 'Deluxe'),
  ]
  name = models.CharField(max_length=50)
  room_type=models.CharField(max_length=10,choices=Room_TYPE_CHOICES)
  price=models.DecimalField(max_digits=7,decimal_places=2)
  is_avaliable=models.BooleanField(default=True)
  


  def __str__(self):
    return self.name
  
class Booking(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE,default=1) 
  customer_name=models.CharField(max_length=100)
  room=models.ForeignKey(Room,on_delete=models.CASCADE)
  check_in=models.DateField()
  check_out=models.DateField()
  booked_at = models.DateTimeField(default=timezone.now) 

  def __str__(self):
      return f"{self.customer_name}-{self.room.name}"
  
# Create your models here.

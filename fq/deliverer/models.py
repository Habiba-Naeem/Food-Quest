from django.db import models
from user.models import *
from cart.models import *

# Create your models here.
class Deliverer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    vehicle_number = models.CharField(max_length = 20)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user}, {self.vehicle_number}, {self.phone_number}"

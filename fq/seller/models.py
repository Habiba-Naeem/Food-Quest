from django.db import models
from user.models import *
# Create your models here.
Restaurant_category = (
    (1, 'American'),
    (2, 'French'),
    (3, 'Chinese'),
    (4, 'Thai'),
    (5, 'Indian'),
    (6, 'Pakistani'),
    (8, 'Italian'),
    (9, 'Japanese'),
    (10, 'Korean'),
    (11, 'Afghani'),
    (12, 'Arabian')
)
Dish_category = (
    (1, "Fast Food"),
    (2, "Savoury"),
    (3, "Dessert"),
    (4, "Breakfast"),
    (5, "Lunch"),
    (6, "Dinner"))

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length = 50)
    category = models.PositiveSmallIntegerField(choices = Restaurant_category)
    picture = models.ImageField(upload_to='dishes/%Y/%m/%d', max_length=255, blank=True, null=True)

    
    def __str__(self):
        return f"{self.name}, {self.address}, {self.category}"


class Seller(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=20)
    restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user}, {self.restaurant}, {self.phone_number}"

class Dish(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    summary = models.CharField(max_length=250)
    nationality = models.PositiveSmallIntegerField(choices=Restaurant_category, default=1)
    no_of_serving = models.PositiveSmallIntegerField()
    picture = models.CharField(max_length=64)
    category = models.PositiveSmallIntegerField(choices=Dish_category, default=1)
    glutten_free = models.BooleanField(default=False)
    customizable = models.BooleanField(default=False)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name="cooks")
    price = models.FloatField()
    picture = models.ImageField(upload_to='dishes/%Y/%m/%d', max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.restaurant}, {self.seller}'s ,{self.name}, {self.picture}, {self.summary}, {self.nationality}, {self.no_of_serving}, {self.picture}, {self.category}, {self.glutten_free}, {self.customizable}, {self.price} "


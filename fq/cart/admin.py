from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.register(Cart)
admin.site.register(Cart_Item)
admin.site.register(Product)
admin.site.register(Order_Items)
admin.site.register(Order)
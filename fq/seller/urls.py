from django.urls import path
from . import views

urlpatterns = [
    path("", views.register, name="register_seller"),
    path("index", views.index, name="seller_index"),  
    path("login", views.login_user, name="login_seller"),
    path("register", views.register, name="register_seller"),
    path("logout", views.logout_user, name="logout_seller"),
    path("additem", views.additem, name="additem"),
    path("getlist", views.getlist, name="getlist"),
    path("get<int:dish_id>", views.getitem, name="getitem"),    
    path("<int:dish_id>", views.redirectitem, name="redirectitem"),
    path("<int:dish_id>/updateitem", views.updateitem, name="updateitem"),
    path("<int:dish_id>/itemupdated", views.itemupdated, name="itemupdated"),
    path("<int:dish_id>/deleteitem", views.deleteitem, name="deleteitem"),
    path("orders", views.display_orders, name="display_orders")
]

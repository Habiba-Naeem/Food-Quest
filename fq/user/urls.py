from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="user_index"), 
    path("login", views.login_user, name="login_user"),
    path("register", views.register, name="register_user"),
    path("logout", views.logout_user, name="logout_user"),
    path("restaurants", views.browseRestaurants, name="browseRestaurants"),
    path("restaurants/<int:category>", views.browseRestaurants_oncategory, name="browseRestaurants_oncategory"),
    path("restaurants/<str:nameof>", views.restaurant, name="restaurant")
]
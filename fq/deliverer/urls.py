from django.urls import path
from . import views

urlpatterns = [
    path("", views.register, name="register_deliverer"),
    path("index", views.index, name="deliverer_index"),  
    path("login", views.login_user, name="login_deliverer"),
    path("register", views.register, name="register_deliverer"),
    path("logout", views.logout_user, name="logout_deliverer"),
    path("<int:id>", views.confirm_delivery, name="confirm_delivery")
]
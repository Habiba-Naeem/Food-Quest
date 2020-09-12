from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="cart"),
    path("cart_item/<item>", views.cart_item, name="cart_item"),
    path("cancel/<int:id>", views.cancel),
    path("quantity/<int:id>/<int:q>", views.quantity, name="quantity"),
    path("order", views.order, name="order"),    
    path("vieworders", views.vieworders, name="vieworders")
    #path("order/<item>", views.order, name="order")
]

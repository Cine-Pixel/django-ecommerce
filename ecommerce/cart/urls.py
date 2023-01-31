from django.urls import path
from .views import view_cart, CartApiView


app_name = "cart"
urlpatterns = [
    path("", view_cart, name="view-cart"),
    path("api/", CartApiView.as_view(), name="cart-api"),
]

from django.urls import path
from .views import place_order, list_orders


app_name = "orders"
urlpatterns = [
    path("create/", place_order, name="place-order"),
    path("", list_orders, name="list-orders"),
]

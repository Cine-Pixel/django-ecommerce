from django.urls import path
from .views import list_products, view_product


app_name = "products"
urlpatterns = [
    path("", list_products, name="list-products"),
    path("<int:pk>/", view_product, name="view-product")
]

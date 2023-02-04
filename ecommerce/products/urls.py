from django.urls import path
from .views import list_products, view_product, home

app_name = "products"
urlpatterns = [
    path("/list-products", list_products, name="list-products"),
    path("<int:pk>/", view_product, name="view-product"),
    path('', home, name='main'),
]

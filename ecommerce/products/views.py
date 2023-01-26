from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .models import Product


def list_products(request: HttpRequest) -> HttpResponse:
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, "products/list_products.html", context=context)


def view_product(request: HttpRequest, pk: int) -> HttpResponse:
    product = Product.objects.filter(id=pk).first()
    if product is None:
        return HttpResponse("<h1>Product not found</h1>")
    context = {
        "product": product
    }
    return render(request, "products/view_product.html", context=context)

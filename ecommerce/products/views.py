from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Product, Category


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


def home(request):
    last_products = Product.objects.filter(quantity=400)
    category_phone = Product.objects.filter(category=1)
    category_laptop = Product.objects.filter(category=2)
    context = {'category_phone': category_phone,
               'category_laptop': category_laptop,
               'last_products': last_products}
    return render(request, 'main.html', context=context)

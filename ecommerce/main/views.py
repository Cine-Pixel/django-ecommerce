from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from products.models import Product


def index(reqeust: HttpRequest) -> HttpResponse:
    top_products = Product.objects.all().order_by("?")[:5]
    context = {
        "top_products": top_products,
        "featured_product": top_products[0]
    }
    return render(reqeust, "main/main.html", context=context)

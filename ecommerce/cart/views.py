from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.db.models import Sum
from products.models import Product
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CartItemSerializer
from .models import Cart


class CartApiView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    def get(self, request: Request) -> Response:
        cart = Cart.objects.get(user = request.user)
        items = cart.items.all()
        data = CartItemSerializer(items, many=True).data
        return Response(data)
    
    def post(self, request: Request) -> Response:
        product_id = request.POST["product_id"]
        cart, _ = Cart.objects.get_or_create(user = request.user)
        product = Product.objects.get(id=product_id)
        _, created = cart.items.get_or_create(product=product)
        data = {"number_of_items_in_cart": cart.items.count()}
        if created:
            data["message"] = "Item added to cart"
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data["message"] = "Item already in cart"
            return Response(data, status=status.HTTP_200_OK)
    
    def put(self, request: Request) -> Response:
        item_id = request.POST["item_id"]
        quantity = request.POST.get("quantity", None)
        try:
            cart = Cart.objects.get(user = request.user)
        except Cart.DoesNotExist:
            return Response(data={"message": "Cart does not exist"}, status=status.HTTP_404_NOT_FOUND)

        item = cart.items.filter(id = item_id).first()
        if item:
            item.quantity = quantity if quantity is not None else (item.quantity + 1)
            item.save()
            return Response(data={"message": f"Added one more {item.product.name}"}, status=status.HTTP_200_OK)
        else:
            return Response(data={"message": "Item not in cart"}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request: Request) -> Response:
        item_id = request.POST["item_id"]
        try:
            cart = Cart.objects.get(user = request.user)
        except Cart.DoesNotExist:
            return Response(data={"message": "Cart does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
        cart.items.filter(id = item_id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def view_cart(request: HttpRequest) -> HttpResponse:
    cart, _ = Cart.objects.get_or_create(user = request.user)
    items = cart.items.all()
    total_price = items.aggregate(Sum("product__price"))["product__price__sum"]
    context = {
        "cart_id": cart.id,
        "cart_items": items,
        "total_price": total_price
    }
    return render(request, "cart/view_cart.html", context=context)

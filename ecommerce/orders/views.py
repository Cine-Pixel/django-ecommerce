from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from products.models import Product
from cart.models import Cart, CartItem
from .models import Order, OrderItem


@login_required(login_url="/users/login")
def place_order(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        cart = Cart.objects.filter(user__id=request.user.id).first()
        if cart is None:
            messages.info("Please add items to the cart to make an order.")
            return redirect("cart:view-cart")
        order_items: list[OrderItem] = []
        for item in cart.items.all():
            product = Product.objects.filter(id=item.product.id).first()
            if product is None or (product.quantity - item.quantity) <= 0:
                messages.info(f"Not enough {product.name}.")
                return redirect("cart:view-cart")
            order_item = OrderItem(product=product, quantity=item.quantity)
            order_items.append(order_item)

        order = Order(user=request.user)
        order.save()
        for item in order_items:
            item.order = order
            item.save()
        cart.delete()
        return redirect("orders:list-orders")
    else:
        return render(request, "errors/not_allowed.html", status=405)


@login_required(login_url="/users/login")
def list_orders(request: HttpRequest) -> HttpResponse:
    if request.method != "GET":
        return render(request, "erros/not_allowed.html", status=405)

    orders = Order.objects.filter(user__id=request.user.id)
    context = {"orders": orders}
    return render(request, "orders/list_orders.html", context=context)

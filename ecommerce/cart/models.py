from django.db import models


class Cart(models.Model):
    user = models.ForeignKey("users.CommerceUser", on_delete=models.CASCADE)
    items: models.QuerySet["CartItem"]

    def __str__(self) -> str:
        return f"{self.user.email}'s cart"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.product.name} - {self.quantity} for {self.cart.user.email}"

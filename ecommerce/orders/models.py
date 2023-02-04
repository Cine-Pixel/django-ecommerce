from django.db import models

# Create your models here.


class Order(models.Model):
    PENDING = "PENDING"
    SHIPPED = "SHIPPED"
    DELIVERED = "DELIVERED"

    STATUS_CHOICES = [
        (PENDING, "Pending"),
        (SHIPPED, "Shipped"),
        (DELIVERED, "Delivered")
    ]

    user = models.ForeignKey("users.CommerceUser", on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)
    items: models.QuerySet["OrderItem"]

    def get_total_price(self):
        return sum([item.product.price * item.quantity for item in self.items.all()])

    def __str__(self):
        return f"{self.status} - {self.user.email}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    quantity = models.IntegerField()

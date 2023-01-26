from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=700)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to="product_images/", default="product_images/default.png")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.image.path

from django.contrib import admin
from .models import Image, Product, Category

class ImageInline(admin.TabularInline):
    model = Image

class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]

admin.site.register(Product, ProductAdmin)
admin.site.register(Image)
admin.site.register(Category)

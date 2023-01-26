from django import forms

from .models import Image, Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ["image"]
        widgets = {
            "image": forms.ClearableFileInput(attrs={"multiple": True}),
        }

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CommerceUser


class CommerceUserCreationForm(UserCreationForm):
    class Meta:
        model = CommerceUser
        fields = ("first_name", "last_name", "email",
                  "password1", "password2", )


class CommerceUserChangeForm(UserChangeForm):
    class Meta:
        model = CommerceUser
        fields = ("email",)

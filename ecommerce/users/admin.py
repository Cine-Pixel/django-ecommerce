from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CommerceUserCreationForm, CommerceUserChangeForm
from .models import CommerceUser


class CustomUserAdmin(UserAdmin):
    add_form = CommerceUserCreationForm
    form = CommerceUserChangeForm
    model = CommerceUser
    list_display = ("email", "first_name", "last_name", "is_staff", "is_active",)
    list_filter = ("email", "first_name", "last_name", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("first_name", "last_name", "email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "first_name", "last_name", "email", "password1", "password2",
                "is_staff", "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("first_name", "last_name", "email",)
    ordering = ("email",)


admin.site.register(CommerceUser, CustomUserAdmin)

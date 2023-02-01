from django.contrib import auth, messages
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views import View
from .forms import CommerceUserCreationForm


class LoginView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "users/login.html")
    
    def post(self, request: HttpRequest) -> HttpResponse:
        username = request.POST.get("email", None)
        password = request.POST.get("password", None)

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now logged in")
            return redirect("products:list-products")
        messages.error(request, "Invalid credentials")
        return redirect("users:login")
    
    
class LogoutView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        auth.logout(request)
        messages.success(request, "You are now logged out")
        
        return redirect("users:login")


class RegisterView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        form = CommerceUserCreationForm()
        context = {
            "form": form
        }
        return render(request, "users/register.html", context=context)
    
    def post(self, request: HttpRequest) -> HttpResponse:
        form = CommerceUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users:login")
        context = {
            "form": form
        }
        return render(request, "users/register.html", context=context)

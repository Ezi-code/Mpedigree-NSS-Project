from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from accounts.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

class LoginView(View):
    def get(self, request):
        return render(request, "accounts/login.html")
    
    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in")
            return redirect("main:list_invoice")
        messages.error(request, "Invalid username or password")
        return render(request, "accounts/login.html")


class SignUpView(View):
    def get(self, request):
        return render(request, "accounts/signup.html")
    
    def post(self, request):
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        if password != password2:
            messages.error(request, "Passwords do not match")
            return render(request, "accounts/signup.html", {"error": "Passwords do not match"})
        user = User.objects.create(username, email, password)
        user.save()
        messages.success(request, "You have successfully signed up")
        return redirect("accounts:login_view")
    


class LogoutView(LoginRequiredMixin,View):
    def get(self, request):
        logout(request)
        messages.success(request, "You have successfully logged out")
        return redirect("accounts:login_view")

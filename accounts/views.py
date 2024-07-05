from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout


class LoginView(View):
    def get(self, request):
        return


class SignUpView(View):
    def get(self, request):
        return


class LogoutView(View):
    def get(self, request):
        return

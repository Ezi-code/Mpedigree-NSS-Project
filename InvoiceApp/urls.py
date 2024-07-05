from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls", namespace="api")),
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path("main/", include("main.urls", namespace="main")),
]

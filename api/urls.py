from rest_framework.urls import path
from api import views

app_name = "api"

urlpatterns = [
    path("list-invoice/", views.ListInvoiceView.as_view(), name="list_invoce"),
]

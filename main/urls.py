from django.urls import path
from . import views


app_name = "main"

urlpatterns = [
    path("create-invoice/", views.CreateInvoiceView.as_view(), name="create_invoice"),
    path("list-invoice/", views.ListInvoiceView.as_view(), name="list_invoice"),
    path(
        "update-invoice/<int:pk>/",
        views.UpdateInvoiceView.as_view(),
        name="update_invoice",
    ),
    path(
        "create-from-csv-upload/",
        views.CreateFromCSVUpload.as_view(),
        name="create_from_csv_upload",
    ),
    path("search-invoice/", views.SearchView.as_view(), name="search_invoice"),
]

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from .forms import InvoceForm
from .models import Invoice
import csv


class CreateInvoiceView(CreateView):
    model = Invoice
    form_class = InvoceForm
    template_name = "main/invoice_form.html"
    success_url = reverse_lazy("main:list_invoice")


class ListInvoiceView(ListView):
    model = Invoice
    template_name = "main/invoice_list.html"
    context_object_name = "invoices"
    paginate_by = 10


class UpdateInvoiceView(UpdateView):
    model = Invoice
    form_class = InvoceForm
    template_name = "main/invoice_form.html"
    success_url = reverse_lazy("main:list_invoice")


class CreateFromCSVUpload(View):
    def get(self, request):
        return render(request, "main/csv_upload.html")

    def post(self, request):
        file = request.FILES["csv_file"]
        data = csv.reader(file.read().decode("utf-8").splitlines())
        for row in data:
            form = InvoceForm(
                {
                    "recipient": row[0],
                    "number_of_items": row[1],
                    "description": row[2],
                    "creation_date": row[3],
                }
            )
            if form.is_valid():
                form.save()
        return redirect("main:list_invoice")
        # return redirect("main:create_from_csv_upload")

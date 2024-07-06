from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .serializer import CSVSerializer, InvoiceSerializer
from main.models import Invoice
from rest_framework.response import Response
from rest_framework import status
import csv
import pandas as pd


class ListInvoiceView(generics.ListAPIView):
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()
    # authentication_classes = [IsAuthenticatedOrReadOnly]


class CreateInvoiceView(generics.CreateAPIView):
    serializer_class = CSVSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        csv_file = serializer.validated_data["csv_file"]
        df = pd.read_csv(csv_file)
        for index, row in df.iterrows():
            new_invoice = Invoice.objects.create(
                recipient=row["recipient"],
                number_of_items=row["number_of_items"],
                description=row["description"],
                creation_date=row["creation_date"],
            )
            new_invoice.clean_fields()
            new_invoice.save()
        return Response({"file saved!"}, status=status.HTTP_201_CREATED)

    # authentication_classes = [IsAuthenticated]

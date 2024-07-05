from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializer import CSVSerializer, InvoiceSerializer
from main.models import Invoice


class ListInvoiceView(generics.ListAPIView):
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()
    authentication_classes = [IsAuthenticatedOrReadOnly]


class CreateInvoiceView(generics.CreateAPIView):
    serializer_class = CSVSerializer
    queryset = Invoice.objects.all()
    authentication_classes = [IsAuthenticatedOrReadOnly]

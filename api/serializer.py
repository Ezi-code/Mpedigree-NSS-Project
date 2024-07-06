from rest_framework import serializers
from main.forms import InvoceForm
from main.models import Invoice
import csv


class CSVSerializer(serializers.Serializer):
    csv_file = serializers.FileField()


class InvoiceSerializer(serializers.ModelSerializer):

    recipient = serializers.CharField(read_only=True)
    number_of_items = serializers.IntegerField(read_only=True)
    description = serializers.CharField(read_only=True)
    creation_date = serializers.DateField(read_only=True)
    expiry_date = serializers.DateField(read_only=True)

    class Meta:
        model = Invoice
        fields = [
            "invoice_code",
            "recipient",
            "number_of_items",
            "description",
            "creation_date",
            "expiry_date",
        ]

from rest_framework import serializers
from main.models import Invoice


class CSVSerializer(serializers.Serializer):
    csv_file = serializers.FileField()


class InvoiceSerializer(serializers.ModelSerializer):
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
        read_only_filed = fields

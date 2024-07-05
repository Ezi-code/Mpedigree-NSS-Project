from rest_framework import serializers
from main.forms import InvoceForm
from main.models import Invoice


class CSVSerializer(serializers.Serializer):
    csv_file = serializers.FileField()

    def create(self, validated_data):
        data = validated_data["csv_file"].read().decode("utf-8").splitlines()
        data = [row for row in data]
        form = InvoceForm(data)
        if form.is_valid():
            form.save()
            return {"message": "Data has been saved successfully."}
        return {"message": "Data is not valid."}


class InvoiceSerializer(serializers.ModelSerializer):
    
    recipient = serializers.CharField(read_only=True)
    number_of_items = serializers.IntegerField(read_only=True)
    description = serializers.CharField(read_only=True)
    creation_date = serializers.DateField(read_only=True)
    expiry_date = serializers.DateField(read_only=True)

    class Meta:
        model = Invoice
        fields = ["recipient", "number_of_items", "description", "creation_date", "expiry_date"]
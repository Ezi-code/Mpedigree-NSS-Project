from django import forms
from main.models import Invoice


class InvoceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            "recipient",
            "number_of_items",
            "description",
            "creation_date",
        ]

        widgets = {
            "creation_date": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "recipient": forms.TextInput(attrs={"class": "form-control"}),
            "number_of_items": forms.NumberInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "cols": 10,
                }
            ),
        }

    def cleaned_date(self):
        cleaned_data = super().clean()
        creation_date = cleaned_data.get("creation_date")
        descriotion = cleaned_data.get("description")
        number_of_items = cleaned_data.get("number_of_items")
        recipient = cleaned_data.get("recipient")
        if not creation_date:
            self.add_error("creation_date", "This field is required")
        if not descriotion:
            self.add_error("description", "This field is required")
        if not number_of_items:
            self.add_error("number_of_items", "This field is required")
        if not recipient:
            self.add_error("recipient", "This field is required")

        return cleaned_data

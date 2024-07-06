from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


class CreateInvoiceViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_invoice(self):
        url = reverse("api:create_invoice")
        data = {
            # Add your request payload here
            "C:\\Users\\Ezi\\Documents\\code\\mpedigree\\InvoiceApp\\data.csv"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Add additional assertions to validate the response data


class ListInvoiceViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_list_invoices(self):
        url = reverse("api:list_invoice")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Add additional assertions to validate the response data

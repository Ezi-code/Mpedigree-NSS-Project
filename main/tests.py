from django.test import TestCase
from main.views import CreateFromCSVUpload, CreateInvoiceView, ListInvoiceView, SearchView, UpdateInvoiceView
from main.models import Invoice
from django.db.models.query import QuerySet
from django.db.models import Q


class CreateInvoiceViewTest(TestCase):
    def test_create_invoice(self):
        view = CreateInvoiceView()
        self.assertEqual(view.model, Invoice)
        self.assertEqual(view.form_class.__name__, "InvoceForm")
        self.assertEqual(view.template_name, "main/invoice_form.html")
        self.assertEqual(view.success_url, "/main/list-invoice/")


class ListInvoiceViewTest(TestCase):
    def test_list_invoice(self):
        view = ListInvoiceView()
        self.assertEqual(view.model, Invoice)
        self.assertEqual(view.template_name, "main/invoice_list.html")
        self.assertEqual(view.context_object_name, "invoices")
        self.assertEqual(view.paginate_by, 12)



class UpdateInvoiceViewTest(TestCase):
    def test_update_invoice(self):
        view = UpdateInvoiceView()
        self.assertEqual(view.model, Invoice)
        self.assertEqual(view.form_class.__name__, "InvoceForm")
        self.assertEqual(view.template_name, "main/invoice_form.html")
        self.assertEqual(view.success_url, "/main/list-invoice/")


class CreateFromCSVUploadTest(TestCase):
    def test_create_from_csv_upload(self):
        view = CreateFromCSVUpload()
        self.assertEqual(view.get(None).status_code, 200)
        self.assertEqual(view.post(None).status_code, 302)


class SearchViewTest(TestCase):
    def test_search_view(self):
        view = SearchView()
        self.assertEqual(view.template_name, "main/invoice_search.html")
        self.assertIsInstance(view.get_queryset(), QuerySet)
        self.assertEqual(view.get_queryset().query.__str__(), "SELECT `main_invoice`.`id`, `main_invoice`.`recipient`, `main_invoice`.`number_of_items`, `main_invoice`.`description`, `main_invoice`.`creation_date` FROM `main_invoice`")
        self.assertEqual(view.get_queryset().count(), 0)
        self.assertEqual(view.get_queryset().query.__str__(), "SELECT `main_invoice`.`id`, `main_invoice`.`recipient`, `main_invoice`.`number_of_items`, `main_invoice`.`description`, `main_invoice`.`creation_date` FROM `main_invoice`")
        self.assertEqual(view.get_queryset().count(), 0)
        self.assertEqual(view.get_queryset().query.__str__(), "SELECT `main_invoice`.`id`, `main_invoice`.`recipient`, `main_invoice`.`number_of_items`, `main_invoice`.`description`, `main_invoice`.`creation_date` FROM `main_invoice`")
        self.assertEqual(view.get_queryset().count(), 0)
        self.assertEqual(view.get_queryset().query.__str__(), "SELECT `main_invoice`.`id`, `main_invoice`.`recipient`, `main_invoice`.`number_of_items`, `main_invoice`.`description`, `main_invoice`.`creation_date` FROM `main_invoice`")
        self.assertEqual(view.get_queryset().count(), 0)
        self.assertEqual(view.get_queryset().query.__str__(), "SELECT `main_invoice`.`id`, `main_invoice`.`recipient`, `main_invoice`.`number_of_items`, `main_invoice`.`description`, `main_invoice`.`creation_date` FROM `main_invoice`")
        self.assertEqual(view.get_queryset().count(), 0)
        self.assertEqual(view.get_queryset().query.__str__(), "SELECT `main_invoice`.`id`, `main_invoice`.`recipient`, `main_invoice`.`number_of_items`, `main_invoice`.`description`, `main_invoice`.`creation_date` FROM `main_invoice`")
        self.assertEqual(view.get_queryset().count(), 0)
        self.assertEqual(view.get_queryset().query.__str__(), "SELECT `main_invoice`.`id`, `main_invoice`.`recipient`, `main_invoice`.`number_of_items`, `main_invoice`.`description`, `main_invoice`.`creation_date` FROM `main_invoice`")
        self.assertEqual(view.get_queryset().count(), 0)
        self.assertEqual(view.get_queryset().count(), 0)
        self.assertEqual(view.get_queryset().count(), 0)
        self.assertEqual(view.get_queryset().count(), 0)
        self.assertEqual(view.get_queryset().count(), 0)
        self.assertEqual(view.get_queryset().count(), 0)
        
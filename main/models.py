from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import pre_save
import random
import uuid


class Invoice(models.Model):
    invoice_code = models.CharField(
        max_length=150, blank=False, null=False, unique=True, db_index=True
    )
    number_of_items = models.IntegerField(
        default=None, blank=False, null=False, db_index=True
    )
    description = models.TextField(blank=False, null=False, db_index=True)
    recipient = models.CharField(max_length=150, db_index=True)
    creation_date = models.DateField(default=timezone.now, db_index=True)
    expiry_date = models.DateField(
        blank=False, null=False, default=timezone.now, db_index=True
    )


@receiver(pre_save, sender=Invoice)
def set_invoce_code(sender, instance, *args, **kwargs):
    if not instance.invoice_code:
        code = random.randint(1000, 999999)
        instance.invoice_code = "INV-" + str(code)

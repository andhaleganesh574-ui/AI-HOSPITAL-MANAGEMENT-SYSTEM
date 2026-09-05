from django.db import models
from patients.models import Patient


class Bill(models.Model):

    PAYMENT_METHODS = [
        ('Cash', 'Cash'),
        ('UPI', 'UPI'),
        ('Card', 'Card'),
        ('Bank Transfer', 'Bank Transfer'),
    ]

    PAYMENT_STATUS = [
        ('Pending', 'Pending'),
        ('Partial', 'Partial'),
        ('Paid', 'Paid'),
    ]

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE
    )

    invoice_number = models.CharField(
        max_length=100,
        unique=True
    )

    consultation_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    medicine_charges = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    laboratory_charges = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    room_charges = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    other_charges = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    discount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    tax = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    paid_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    payment_method = models.CharField(
        max_length=50,
        choices=PAYMENT_METHODS,
        default='Cash'
    )

    payment_status = models.CharField(
        max_length=30,
        choices=PAYMENT_STATUS,
        default='Pending'
    )

    bill_date = models.DateField(
        auto_now_add=True
    )

    notes = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.invoice_number
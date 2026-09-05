from django.db import models
from patients.models import Patient
from doctors.models import Doctor


class LabTest(models.Model):

    TEST_STATUS = [
        ('Pending', 'Pending'),
        ('Sample Collected', 'Sample Collected'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    test_name = models.CharField(max_length=150)

    test_category = models.CharField(
        max_length=100
    )

    sample_type = models.CharField(
        max_length=100
    )

    test_date = models.DateField()

    result = models.TextField(
        blank=True
    )

    normal_range = models.CharField(
        max_length=150,
        blank=True
    )

    remarks = models.TextField(
        blank=True
    )

    status = models.CharField(
        max_length=50,
        choices=TEST_STATUS,
        default='Pending'
    )

    report_number = models.CharField(
        max_length=100,
        unique=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.report_number} - {self.test_name}"
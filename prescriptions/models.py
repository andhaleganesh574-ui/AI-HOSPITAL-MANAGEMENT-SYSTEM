from django.db import models
from patients.models import Patient
from doctors.models import Doctor
from pharmacy.models import Medicine


class Prescription(models.Model):

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE
    )

    medicine = models.ForeignKey(
        Medicine,
        on_delete=models.CASCADE
    )

    dosage = models.CharField(max_length=100)

    frequency = models.CharField(max_length=100)

    duration = models.CharField(max_length=100)

    instructions = models.TextField(blank=True)

    prescribed_date = models.DateField(
        auto_now_add=True
    )

    status = models.CharField(
        max_length=30,
        default='Active'
    )

    def __str__(self):
        return f"{self.patient.name} - {self.medicine.name}"
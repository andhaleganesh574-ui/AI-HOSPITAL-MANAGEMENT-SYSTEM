from django.db import models
from admin_panel.models import Department


class Doctor(models.Model):

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    specialization = models.CharField(max_length=100)
    qualification = models.CharField(max_length=150)
    experience = models.PositiveIntegerField(default=0)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='doctors'
    )
    consultation_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    available = models.BooleanField(default=True)
    profile_image = models.ImageField(
        upload_to='doctors/',
        blank=True,
        null=True
    )

    def __str__(self):
        return f"Dr. {self.name}"


class Prescription(models.Model):

    appointment = models.ForeignKey(
        'appointments.Appointment',
        on_delete=models.CASCADE,
        related_name='prescriptions'
    )

    medicine = models.ForeignKey(
        'pharmacy.Medicine',
        on_delete=models.CASCADE,
        related_name='prescriptions'
    )

    dosage = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    instructions = models.TextField(blank=True)

    prescribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.medicine.name} - {self.appointment.patient.name}"
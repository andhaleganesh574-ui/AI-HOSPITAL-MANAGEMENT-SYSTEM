from django.db import models


class Prediction(models.Model):

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    RISK_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    patient_name = models.CharField(
        max_length=150
    )

    age = models.PositiveIntegerField()

    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES
    )

    temperature = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    blood_pressure = models.CharField(
        max_length=20
    )

    blood_sugar = models.DecimalField(
        max_digits=7,
        decimal_places=2
    )

    heart_rate = models.PositiveIntegerField()

    symptoms = models.TextField()

    predicted_disease = models.CharField(
        max_length=150
    )

    risk_level = models.CharField(
        max_length=20,
        choices=RISK_CHOICES
    )

    confidence = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    recommendation = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.patient_name
from django.db import models


class Patient(models.Model):

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    blood_group = models.CharField(
        max_length=5,
        choices=BLOOD_GROUP_CHOICES
    )
    address = models.TextField()
    emergency_contact = models.CharField(max_length=15)
    registered_at = models.DateTimeField(auto_now_add=True)
    profile_image = models.ImageField(
        upload_to='patients/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

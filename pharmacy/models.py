from django.db import models


class Medicine(models.Model):

    CATEGORY_CHOICES = [
        ('Tablet', 'Tablet'),
        ('Capsule', 'Capsule'),
        ('Syrup', 'Syrup'),
        ('Injection', 'Injection'),
        ('Cream', 'Cream'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=150)
    generic_name = models.CharField(max_length=150)
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )
    manufacturer = models.CharField(max_length=150)
    batch_number = models.CharField(max_length=100)
    expiry_date = models.DateField()
    quantity = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=0)
    stock_in = models.PositiveIntegerField(default=0)
    stock_out = models.PositiveIntegerField(default=0)
    reorder_level = models.PositiveIntegerField(default=10)
    reorder_level = models.PositiveIntegerField(default=10)
    purchase_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    selling_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    supplier = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    stock_in = models.PositiveIntegerField(default=0)
    stock_out = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
from django.db import models
from customer.models import Customer


class Account(models.Model):
    ACCOUNT_STATUS_CHOICES = [
        ('active', 'ACTIVE'),
        ('inactive', 'INACTIVE'),
        ('suspended', 'SUSPENDED'),
        ('closed', 'CLOSED'),
    ]

    account_number = models.CharField(max_length=20, unique=True)
    bank_code = models.CharField(max_length=10)
    bank_name = models.CharField(max_length=100)
    customer_id = models.ForeignKey(Customer, related_name="customer", on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=ACCOUNT_STATUS_CHOICES, default='pending')
    assigned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.account_number
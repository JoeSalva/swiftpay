from django.db import models
import uuid
from customer.models import Customer

# Create your models here.

class Wallet(models.Model):
    CURRENCY_CHOICES = [
        ('ngn', 'NGN'), 
        ('usd', 'USD'),
    ]

    wallet_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    customer_id = models.ForeignKey(Customer, related_name='customer', on_delete=models.CASCADE)
    available_balance = models.IntegerField(max_length=12)
    ledger_balance = models.IntegerField(max_length=12)
    currency = models.CharField(choices=CURRENCY_CHOICES, default='ngn')
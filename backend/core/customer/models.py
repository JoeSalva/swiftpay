import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Customer(AbstractUser):
    CUSTOMER_STATUS = [
        ('pending', 'PENDING'),
        ('active', 'ACTIVE'),
        ('suspended', 'SUSPENDED'),
        ('blacklisted', 'BLACKLISTED'),
        ('closed', 'CLOSED'),
    ]

    customer_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    legal_name = models.CharField(max_length=25)
    display_name = models.CharField(max_length=25)
    phone = models.IntegerField(max_length=10)
    email = models.EmailField()
    status = models.CharField(choices=CUSTOMER_STATUS, default='active')
    kyc_tier = None
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)
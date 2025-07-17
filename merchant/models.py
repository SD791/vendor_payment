from django.db import models

class Merchant(models.Model):
    name = models.CharField(max_length=100)
    wallet_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
from django.db import models

# Create your models here.

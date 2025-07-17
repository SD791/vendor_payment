from django.db import models

# Create your models here.
from django.db import models

class Transaction(models.Model):
    order_id = models.IntegerField()
    customer_id = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    platform_fee = models.DecimalField(max_digits=10, decimal_places=2)
    vendorpay_fee = models.DecimalField(max_digits=10, decimal_places=2)
    merchant_share = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

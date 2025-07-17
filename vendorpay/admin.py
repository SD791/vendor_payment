from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'order_id', 'customer_id', 'amount',
        'platform_fee', 'vendorpay_fee', 'merchant_share', 'created_at'
    ]

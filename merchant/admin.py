from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Merchant

@admin.register(Merchant)
class MerchantAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'wallet_balance']

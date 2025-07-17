from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
        read_only_fields = ['platform_fee', 'vendorpay_fee', 'merchant_share', 'created_at']

    def create(self, validated_data):
        amount = validated_data['amount']
        validated_data['platform_fee'] = round(amount * 0.05, 2)
        validated_data['vendorpay_fee'] = round(amount * 0.05, 2)
        validated_data['merchant_share'] = round(amount * 0.90, 2)
        return super().create(validated_data)

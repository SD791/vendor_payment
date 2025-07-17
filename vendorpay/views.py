from rest_framework.decorators import api_view
from rest_framework.response import Response
from vendorpay.models import Transaction
from merchant.models import Merchant
from amazon.models import Order
from vendorpay.serializers import TransactionSerializer
from django.db import transaction as db_transaction


@api_view(['POST'])
def process_payment(request):
    order_id = request.data.get('order_id')

    try:
        order = Order.objects.using('amazon_db').get(id=order_id)
        total = order.total_price

        # Calculate fees
        platform_fee = round(total * 0.05, 2)
        vendorpay_fee = round(total * 0.05, 2)
        merchant_share = round(total - platform_fee - vendorpay_fee, 2)

        # Save transaction in vendorpay_db
        txn = Transaction.objects.using('vendorpay_db').create(
            order_id=order.id,
            customer_id=order.customer.id,
            amount=total,
            platform_fee=platform_fee,
            vendorpay_fee=vendorpay_fee,
            merchant_share=merchant_share
        )

        # Update merchant wallet in merchant_db
        merchant = Merchant.objects.using('merchant_db').first()
        merchant.wallet_balance += merchant_share
        merchant.save(using='merchant_db')

        return Response({
            "status": "success",
            "transaction_id": txn.id,
            "order_id": order.id,
            "amount": float(total),
            "platform_fee": float(platform_fee),
            "vendorpay_fee": float(vendorpay_fee),
            "merchant_share": float(merchant_share),
            "wallet_updated": True
        })

    except Order.DoesNotExist:
        return Response({"status": "error", "message": "Order not found"}, status=404)


@api_view(['POST'])
def create_transaction(request):
    serializer = TransactionSerializer(data=request.data)
    if serializer.is_valid():
        obj = serializer.save()  # Save without specifying DB
        obj.save(using='vendorpay_db')  # Save to vendorpay database explicitly
        return Response(TransactionSerializer(obj).data)
    return Response(serializer.errors, status=400)

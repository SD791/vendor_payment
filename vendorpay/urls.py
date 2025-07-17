from django.urls import path
from .views import process_payment, create_transaction

urlpatterns = [
    path('transaction/create/', create_transaction, name='create_transaction'),
    path('transaction/process/', process_payment, name='process_payment'),
]

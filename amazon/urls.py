from django.urls import path
from .views import customer_list_create, product_list_create, order_list_create
from . import views
urlpatterns = [
    path('customers/', customer_list_create),
    path('products/', product_list_create),
    path('orders/', order_list_create),

]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/', views.product_view, name='product'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('success/', views.success_view, name='success'),
]

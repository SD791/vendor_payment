from django.urls import path
from .views import create_merchant

urlpatterns = [
    path('create/', create_merchant),
]
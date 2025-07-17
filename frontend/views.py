from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def product_view(request):
    return render(request, 'product.html')

def checkout_view(request):
    return render(request, 'checkout.html')

def success_view(request):
    return render(request, 'success.html')

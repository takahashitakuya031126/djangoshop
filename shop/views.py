from django.shortcuts import render
from shop.models import Product

def all_products(request):
    products = Product.valid_objects.all()
    return render(request, 'shop/product_list.html', {'products': products})
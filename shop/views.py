from django.shortcuts import render

def all_products(request):
    return render(request, 'shop/product_list.html', {})
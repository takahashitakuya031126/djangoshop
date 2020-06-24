from django.shortcuts import render
from shop.models import Product
from django.core.paginator import Paginator, EmptyPage, InvalidPage

def all_products(request):
    products_list = Product.valid_objects.all()
    
    paginator = Paginator(products_list, 3)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
 
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)
 
    return render(request, 'shop/product_list.html', {'products': products})


def product_detail(request, product_slug):
    try:
        product = Product.objects.get(slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'shop/product_detail.html', {'product': product})
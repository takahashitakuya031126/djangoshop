from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def all_products(request):
    return HttpResponse('This is a Top page')
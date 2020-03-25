from django.shortcuts import render
from api.models import Product, Category
from django.http import JsonResponse


def products_list(request):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)


def categories_list(request):
    pass


def category_detail(request):
    pass


def category_products(request):
    pass

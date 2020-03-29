from django.shortcuts import render
from api.models import Product, Category
from django.http import JsonResponse


def products_list(request):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)


def categories_list(request):
    categories = Category.objects.all()
    categories_json = [category.to_json() for category in categories]
    return JsonResponse(categories_json, safe=False)


def category_detail(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
        # raise Http404

    return JsonResponse(category.to_json())


def category_products(request, category_id):
    category_prod = Product.objects.all().filter(category_id=category_id)
    cat_prod_json = [product.to_json() for product in category_prod]
    return JsonResponse(cat_prod_json, safe=False)

from django.urls import path

from api.views import products_list, categories_list, category_detail, category_products

urlpatterns = [
    # /api/products - List of all Products
    #     # /api/products/<int:id>/ - Get one Product
    #     # /api/categories/ - List of all Categories
    #     # /api/categories/<int:id>/ - Get one Category
    #     # /api/categories/<int:id>/products/ - List of Products by Category
    path('products/', products_list),
    path('categories/', categories_list),
    path('categories/<int:id>', category_detail),
    path('categories/<int:id/products>', category_products)
]

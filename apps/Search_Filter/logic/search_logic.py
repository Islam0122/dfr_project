from apps.Products.models import Product
from apps.Sellers.models import SellerProfile


def search_products(query):
    product_results = Product.objects.filter(name__icontains=query) | Product.objects.filter(price__icontains=query)
    return product_results


def search_sellers(query):
    sellers_results = (SellerProfile.objects.filter(name__icontains=query))
    return sellers_results
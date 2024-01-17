# search/urls.py

from django.urls import path
from .views import SearchProductView, SearchSellerView, FilterProductView

urlpatterns = [
    path('search_product/', SearchProductView.as_view(), name='search-product-view'),
    path('search_seller/', SearchSellerView.as_view(), name='search-seller-view'),
    path('filter_products/', FilterProductView.as_view(), name='filter-products')

]

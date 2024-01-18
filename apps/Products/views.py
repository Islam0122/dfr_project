from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_create(self, serializer):
        # При создании товара устанавливаем user в текущего пользователя
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Product.objects.all()

class RecommendedProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    def get_queryset(self):
        return Product.objects.filter(is_recommended=True)

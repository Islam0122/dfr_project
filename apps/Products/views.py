from rest_framework import viewsets
from .models import Product
from .serializers import ProductWithLessonCountSerializer

class ProductWithLessonCountViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductWithLessonCountSerializer
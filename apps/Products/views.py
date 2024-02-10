from django.shortcuts import render
from rest_framework import viewsets, status
from .models.models import *
from .serializers import *


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

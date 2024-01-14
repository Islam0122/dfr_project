from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Service
from .serializers import ServiceSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = 'pk'


class RecommendedServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return Service.objects.filter(is_recommended=True)

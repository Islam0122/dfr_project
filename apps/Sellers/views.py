from django.shortcuts import render
from rest_framework import viewsets, status
from .models import SellerProfile
from .serializers import SellerProfileSerializer


class SellerProfileViewSet(viewsets.ModelViewSet):
    queryset = SellerProfile.objects.all()
    serializer_class = SellerProfileSerializer
    lookup_field = 'pk'

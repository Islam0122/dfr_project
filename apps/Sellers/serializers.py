from rest_framework import serializers
from .models import SellerProfile
from ..Products.serializers import ProductSerializer


class SellerProfileSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    products = ProductSerializer(many=True, read_only=True, source='user.products')

    class Meta:
        model = SellerProfile
        fields = ['id', 'user', 'logo', 'name', 'description', 'phone_number', 'address', 'email', 'whatsapp_number',
                  'instagram_url', 'telegram_url', 'website', 'products']
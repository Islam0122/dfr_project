from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='title', queryset=Category.objects.all())
    class Meta:
        model = Product
        fields = ['name','img1','img2','img3','img4','category','description','price']
        read_only_fields = ('created_at', 'updated_at')

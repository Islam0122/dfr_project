from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='title', queryset=Category.objects.all())
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Product
        fields = ['name',
                  'img1','img2','img3','img4',
                  'category','description','price','user','created_at', 'updated_at']
        read_only_fields = ('created_at', 'updated_at','user')

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return Product.objects.create(**validated_data)
from rest_framework import serializers
from .models.models import Category


# Category
class CategorySerializer(serializers.ModelSerializer):
    parent_category = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'title', 'parent_category')
    def get_parent_category(self, obj):
        return obj.parent_category.title if obj.parent_category else None

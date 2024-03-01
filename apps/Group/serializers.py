from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Group

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
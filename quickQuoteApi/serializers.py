# import something copilot!
from rest_framework.serializers import ModelSerializer
from django.conf import settings
from rest_framework import serializers
from .models import Product 


class ProductSerializer(ModelSerializer):
    image_field = serializers.ImageField(max_length=None)
    class Meta:
        model = Product
        fields = '__all__'


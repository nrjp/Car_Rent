from rest_framework import serializers
from .models import CarCategory

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarCategory
        fields = ['category']
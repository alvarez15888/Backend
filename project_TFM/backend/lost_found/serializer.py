from rest_framework import serializers

from .models import Lost, Found

class LostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lost
        fields = '__all__'

class FoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Found
        fields = '__all__'
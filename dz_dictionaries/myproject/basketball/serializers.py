from rest_framework import serializers
from .models import BasketballPlayer

class BasketballPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketballPlayer
        fields = '__all__'

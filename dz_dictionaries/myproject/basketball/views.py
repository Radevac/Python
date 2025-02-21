from django.shortcuts import render

from rest_framework import viewsets
from .models import BasketballPlayer
from .serializers import BasketballPlayerSerializer

class BasketballPlayerViewSet(viewsets.ModelViewSet):
    queryset = BasketballPlayer.objects.all()
    serializer_class = BasketballPlayerSerializer


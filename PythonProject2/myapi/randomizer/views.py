from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
import random

@api_view(['GET'])
def get_random_number(request):
    return Response({"number": random.randint(1, 100)})

@api_view(['GET'])
def get_random_range(request):
    min_val = int(request.GET.get('min', 1))
    max_val = int(request.GET.get('max', 100))
    return Response({"number": random.randint(min_val, max_val)})

@api_view(['GET'])
def get_random_set(request):
    count = int(request.GET.get('n', 5))
    numbers = [random.randint(1, 100) for _ in range(count)]
    return Response({"numbers": numbers})


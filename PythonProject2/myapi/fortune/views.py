from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
import random

FORTUNES = [
    "Сьогодні твій день!",
    "Будь уважний до дрібниць.",
    "Найкраще ще попереду.",
    "Посмішка принесе удачу!"
]

@api_view(['GET'])
def get_fortune(request):
    return Response({"fortune": random.choice(FORTUNES)})


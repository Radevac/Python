from django.urls import path
from .views import get_fortune

urlpatterns = [
    path('fortune/', get_fortune),
]

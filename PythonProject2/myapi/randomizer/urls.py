from django.urls import path
from .views import get_random_number, get_random_range, get_random_set

urlpatterns = [
    path('random/', get_random_number),
    path('random/range/', get_random_range),
    path('random/set/', get_random_set),
]

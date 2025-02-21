from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BasketballPlayerViewSet

router = DefaultRouter()
router.register(r'', BasketballPlayerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

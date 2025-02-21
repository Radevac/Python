from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DictionaryViewSet

router = DefaultRouter()
router.register(r'', DictionaryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

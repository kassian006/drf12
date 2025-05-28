from django.urls import path, include
from .views import CarViewSet, BrandViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'brand', BrandViewSet, basename='brands'),
router.register(r'car', CarViewSet, basename='cars'),

urlpatterns = [
    path('', include(router.urls)),
]
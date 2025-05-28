from django_filters import FilterSet
from .models import Car, Brand, CarModel


class CarFilter(FilterSet):
    class Meta:
        model = Car
        fields = {
            'year': ['exact'],
            'price': ['gt', 'lt'],
        }


class BrandFilter(FilterSet):
    class Meta:
        model = Brand
        fields = {
            'brand_name': ['exact'],
        }

class CarModelFilter(FilterSet):
    class Meta:
        model = CarModel
        fields = {
            'car_model': ['exact'],
        }
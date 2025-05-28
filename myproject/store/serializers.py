from rest_framework import serializers
from .models import Brand, CarModel, Car


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields  = '__all__'


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'car_name', 'price', 'year', 'rul', 'city', 'car_image',
                  'car_video', 'create_date', 'brand', 'car']



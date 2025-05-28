from django.db import models


class Brand(models.Model):
    brand_color = models.ImageField(upload_to='brand_image/')
    brand_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.brand_name


class CarModel(models.Model):
    car_model = models.CharField(max_length=10, unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.car_model


class Car(models.Model):
    car_name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.PositiveSmallIntegerField(null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    RUL_CHOICES = (
        ('left', 'left'),
        ('right', 'right')
    )
    rul = models.CharField(max_length=32, choices=RUL_CHOICES)
    city = models.CharField(max_length=32)
    car_image = models.ImageField(upload_to='car_images/', null=True, blank=True)
    car_video = models.FileField(upload_to='car_videos',
                                 null=True, blank=True, verbose_name='Видео')
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.car_name}-{self.price}'
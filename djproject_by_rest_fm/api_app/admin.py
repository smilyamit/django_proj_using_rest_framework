from django.contrib import admin

# Register your models here.

from .models import Car, Bike, MotorBike, BlogModel
admin.site.register(Car)
admin.site.register(Bike)
admin.site.register(MotorBike)
admin.site.register(BlogModel)

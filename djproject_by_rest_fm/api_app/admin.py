from django.contrib import admin

# Register your models here.

from .models import Car, Bike
admin.site.register(Car)
admin.site.register(Bike)

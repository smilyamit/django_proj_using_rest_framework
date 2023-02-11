from django.forms import ModelForm
from .models import Car, Bike

class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ('car_name', 'car_model', 'car_color')

# class BikeForm(ModelForm):
#     class Meta:
#         model = Bike
#         fields = ('bike_name', 'bike_model', 'bike_color')

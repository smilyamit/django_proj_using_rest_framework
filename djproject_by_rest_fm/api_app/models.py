from django.db import models


class Car(models.Model):
    car_name = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    car_color = models.CharField(max_length=20)

    class Meta:  # This is optional and is used to change the name of the table in the database
        db_table = 'car'
        verbose_name = 'Special Car'

    def __str__(self):
        return self.car_name


class Bike(models.Model):
    bike_name = models.CharField(max_length=100)
    bike_model = models.CharField(max_length=100)
    bike_color = models.CharField(max_length=20)

    class Meta:
        db_table = 'bike'
        verbose_name = 'Bike List'

    def __str__(self):
        return self.bike_name

class MotorBike(models.Model):
    motor_bike_name = models.CharField(max_length=100)
    motor_bike_model = models.CharField(max_length=100)
    motor_bike_color = models.CharField(max_length=20)

    class Meta:
        db_table = 'motor bike'
        verbose_name = 'Motor Bike List'

    def __str__(self):
        return self.motor_bike_name


class BlogModel(models.Model):
    title = models.CharField(max_length=1000)
    content = models.TextField(blank=True)
    def __str__(self):
        return self.title

from django.db import models

class Car(models.Model):
    car_name = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    car_color = models.CharField(max_length=20)

    class Meta:    # This is optional and is used to change the name of the table in the database
        db_table = 'car'
        verbose_name = 'Specialcar'

    def __str__(self):
        return self.car_name
    


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('car_name/<int:pk>/', views.add_car, name='car_name'),
    path('car_name/', views.add_car, name='car_name'),
]

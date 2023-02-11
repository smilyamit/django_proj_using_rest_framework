from django.urls import path
from . import views
from . import genericViews

urlpatterns = [
    path('', views.index, name='index'),
    # path('car_name/<int:pk>/', views.add_car, name='car_name'),
    path('car_name/', views.add_car, name='car_name'),
    path('car_class/', views.CarView.as_view()),
    path('bike_list/', genericViews.BikeListView.as_view(), name="bike_related"),
]

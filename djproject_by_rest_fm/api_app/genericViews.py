from django.views import View
from .models import Bike, MotorBike
from django.shortcuts import render
from django.views import generic


#custom made generic ListView
class BikeListView(View):
    model = Bike

    def get(self, request):
        modelName = self.model.__name__.lower()
        stuff = self.model.objects.all()
        cntx = {modelName + '_list': stuff}     # modelName + '_list' gives here bike_list
        return render(request, 'api_app/' + modelName + '_list.html', cntx)


#actual generic class based ListView
class MotorBikeListView(generic.ListView):
    model = MotorBike
    # modelName + '_list' gives here motorbike_list, it will be done automatically by ListView method of generic class

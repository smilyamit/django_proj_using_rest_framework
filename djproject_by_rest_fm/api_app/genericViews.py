from django.views import View
from .models import Bike
from django.shortcuts import render


class BikeListView(View):
    model = Bike

    def get(self, request):
        modelName = self.model.__name__.lower()
        stuff = self.model.objects.all()
        cntx = {modelName + '_list': stuff}
        return render(request, 'api_app/' + modelName + '_list.html', cntx)

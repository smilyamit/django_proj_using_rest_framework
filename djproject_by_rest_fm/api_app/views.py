from django.shortcuts import render, redirect
from .forms import CarForm
from .models import Car

#get request
def index(request):
    form = CarForm()
    return render(request, 'api_app/carName.html', {'form': form})


#post request
def add_car(request):
    if request.method == 'POST':
        # car = Car.objects.all().first()
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CarForm()
    
    context = {'form': form}

    return render(request, 'api_app/carName.html', context)
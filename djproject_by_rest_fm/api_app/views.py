from django.shortcuts import render, redirect
from .forms import CarForm
from .models import Car
from django.views import View


# get request
def index(request):
    form = CarForm()
    return render(request, 'api_app/carName.html', {'form': form})


# post request  using normal view functiom/method
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


# POST request using class based views
class CarView(View):
    form_class = CarForm    # class variables
    template_name = "api_app/carName.html"
    def get(self, request):
        form = self.form_class()
        context = {"form": form}

        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = self.form_class()
        context = {'form': form}
        return render(request, self.template_name, context)

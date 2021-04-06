from django.shortcuts import render
from .models import Team
from cars.models import Car
# Create your views here.


def index(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    data = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
    }
    return render(request, 'page/index.html', data)


def about(request):
    return render(request, 'page/about.html')


def contact(request):
    return render(request, 'page/contact.html')


def services(request):
    return render(request, 'page/services.html')

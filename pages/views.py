from django.shortcuts import render
from .models import Team

# Create your views here.


def index(request):
    teams = Team.objects.all()
    data = {
        teams: 'teams',
    }
    return render(request, 'page/index.html', data)


def about(request):
    return render(request, 'page/about.html')


def contact(request):
    return render(request, 'page/contact.html')


def services(request):
    return render(request, 'page/services.html')

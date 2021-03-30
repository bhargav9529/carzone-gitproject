from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'page/index.html')


def about(request):
    return render(request, 'page/about.html')


def contact(request):
    return render(request, 'page/contact.html')


def services(request):
    return render(request, 'page/services.html')

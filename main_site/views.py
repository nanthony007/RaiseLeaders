from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'main_site/home.html')


def curriculum(request):
    return render(request, 'main_site/curriculum.html')


def library(request):
    return render(request, 'main_site/library.html')


def calendar(request):
    return render(request, 'main_site/calendar.html')


def contact(request):
    return render(request, 'main_site/contact.html')

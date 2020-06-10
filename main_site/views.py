from django.shortcuts import render

# Create your views here.


def about(request):
    return render(request, 'main_site/about.html')


def curriculum(request):
    return render(request, 'main_site/curriculum.html')


def library(request):
    return render(request, 'main_site/library.html')


def calendar(request):
    return render(request, 'main_site/calendar.html')


def terminology(request):
    return render(request, 'main_site/terminology.html')


def strikes(request):
    return render(request, 'main_site/strikes.html')


def forms(request):
    return render(request, 'main_site/forms.html')


def workouts(request):
    return render(request, 'main_site/workouts.html')


def acrobatics(request):
    return render(request, 'main_site/acrobatics.html')


def extras(request):
    return render(request, 'main_site/extras.html')

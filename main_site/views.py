from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.

def about(request):
    if not request.user.is_authenticated:
        messages.error(request, f"You need to be logged in to see this page.  Please login or register.")
        return redirect('login')
    return render(request, 'main_site/about.html')


def curriculum(request):
    if not request.user.is_authenticated:
        messages.error(request, f"You need to be logged in to see this page.  Please login or register.")
        return redirect('login')
    return render(request, 'main_site/curriculum.html')


def library(request):
    if not request.user.is_authenticated:
        messages.error(request, f"You need to be logged in to see this page.  Please login or register.")
        return redirect('login')
    return render(request, 'main_site/library.html')


def calendar(request):
    if not request.user.is_authenticated:
        messages.error(request, f"You need to be logged in to see this page.  Please login or register.")
        return redirect('login')
    return render(request, 'main_site/calendar.html')


def terminology(request):
    if not request.user.is_authenticated:
        messages.error(request, f"You need to be logged in to see this page.  Please login or register.")
        return redirect('login')
    return render(request, 'main_site/terminology.html')


def strikes(request):
    if not request.user.is_authenticated:
        messages.error(request, f"You need to be logged in to see this page.  Please login or register.")
        return redirect('login')
    return render(request, 'main_site/strikes.html')


def tkd_forms(request):
    if not request.user.is_authenticated:
        messages.error(request, f"You need to be logged in to see this page.  Please login or register.")
        return redirect('login')
    return render(request, 'main_site/tkd_forms.html')


def workouts(request):
    if not request.user.is_authenticated:
        messages.error(request, f"You need to be logged in to see this page.  Please login or register.")
        return redirect('login')
    return render(request, 'main_site/workouts.html')


def acrobatics(request):
    if not request.user.is_authenticated:
        messages.error(request, f"You need to be logged in to see this page.  Please login or register.")
        return redirect('login')
    return render(request, 'main_site/acrobatics.html')


def extras(request):
    if not request.user.is_authenticated:
        messages.error(request, f"You need to be logged in to see this page.  Please login or register.")
        return redirect('login')
    return render(request, 'main_site/extras.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.list import ListView

from .models import Resource


# Create your views here.

def about(request):
    if not request.user.is_authenticated:
        messages.error(request, f"You need to be logged in to see this page.  Please login or register.")
        return redirect('login')
    return render(request, 'main_site/about.html')


class CurriculumnListView(ListView):
    model = Resource
    template_name = 'main_site/curriculum.html'
    
    def get_queryset(self):
        qs = Resource.objects.filter(belt_level=self.request.user.profile.belt).order_by('title')
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.request.user.is_authenticated:
            messages.error(self.request, f"You need to be logged in to see this page.  Please login or register.")
            return redirect('login')
        return context




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

from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.list import ListView

from .models import Resource, NinjaItem


# Create your views here.


def about(request):
    if not request.user.is_authenticated:
        messages.error(
            request,
            f"You need to be logged in to see this page.  Please login or register.",
        )
        return redirect("login")
    return render(request, "main_site/about.html")


class CurriculumnListView(ListView):
    model = Resource
    template_name = "main_site/curriculum.html"

    def get_queryset(self):
        qs = (
            Resource.objects.filter(curriculum=True)
            .filter(belt_level=self.request.user.profile.belt)
            .order_by("title")
        )
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.request.user.is_authenticated:
            messages.error(
                self.request,
                f"You need to be logged in to see this page.  Please login or register.",
            )
            return redirect("login")
        return context


def library(request):
    if not request.user.is_authenticated:
        messages.error(
            request,
            f"You need to be logged in to see this page.  Please login or register.",
        )
        return redirect("login")
    return render(request, "main_site/library.html")


class LibraryCategory(ListView):
    model = Resource
    template_name = "main_site/library_category.html"

    def get_queryset(self, **kwargs):
        cat = self.kwargs.get("category")
        if cat == "poomsae" or cat == "exercises":
            qs = Resource.objects.filter(curriculum=False).filter(
                category=cat.capitalize()
            )
            return qs
        else:
            qs = Resource.objects.filter(category=cat.capitalize()).order_by("title")
            return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_name"] = self.kwargs.get("category").capitalize()
        return context


def calendar(request):
    if not request.user.is_authenticated:
        messages.error(
            request,
            f"You need to be logged in to see this page.  Please login or register.",
        )
        return redirect("login")
    return render(request, "main_site/calendar.html")


class NinjaBoard(ListView):
    model = NinjaItem
    template_name = "main_site/ninjaboard.html"

    def get_queryset(self):
        qs = NinjaItem.objects.all().order_by("-date")
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.request.user.is_authenticated:
            messages.error(
                self.request,
                f"You need to be logged in to see this page.  Please login or register.",
            )
            return redirect("login")
        return context

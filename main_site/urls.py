from django.urls import path

from . import views

urlpatterns = [
    path('curriculum/', views.curriculum, name='curriculum'),
    path('contact/', views.contact, name='contact'),
    path('calendar/', views.calendar, name='calendar'),
    path('library/', views.library, name='library'),
]
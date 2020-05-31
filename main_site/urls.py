from django.urls import path

from . import views

urlpatterns = [
    path('curriculum/', views.curriculum, name='curriculum'),
    path('contact/', views.contact, name='contact'),
    path('calendar/', views.calendar, name='calendar'),
    path('library/', views.library, name='library'),
    path('library/terminology/', views.terminology, name='terminology'),
    path('library/strikes/', views.strikes, name='strikes'),
    path('library/forms/', views.forms, name='forms'),
    path('library/workouts/', views.workouts, name='workouts'),
    path('library/acrobatics/', views.acrobatics, name='acrobatics'),
    path('library/extras/', views.extras, name='extras'),
    path('about/', views.about, name='about'),
]
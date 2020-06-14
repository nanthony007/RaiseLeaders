from django.urls import path

from . import views

urlpatterns = [
    path('curriculum/', views.CurriculumnListView.as_view(), name='curriculum'),
    path('about/', views.about, name='about'),
    path('calendar/', views.calendar, name='calendar'),
    path('library/', views.library, name='library'),
    path('library/terminology/', views.terminology, name='terminology'),
    path('library/strikes/', views.strikes, name='strikes'),
    path('library/tkd_forms/', views.tkd_forms, name='tkd_forms'),
    path('library/workouts/', views.workouts, name='workouts'),
    path('library/acrobatics/', views.acrobatics, name='acrobatics'),
    path('library/extras/', views.extras, name='extras'),
]
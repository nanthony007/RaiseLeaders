from django.urls import path

from . import views

urlpatterns = [
    path('curriculum/', views.CurriculumnListView.as_view(), name='curriculum'),
    path('about/', views.about, name='about'),
    path('calendar/', views.calendar, name='calendar'),
    path('library/', views.library, name='library'),
    path('library/<str:category>/', views.LibraryCategory.as_view(), name='category_view'),
]
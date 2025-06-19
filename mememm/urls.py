from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('toys/', views.toys, name='toys'),
    path('contacts/', views.contacts, name='contacts'),

]
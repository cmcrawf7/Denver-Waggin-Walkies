from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    
    # path('login/', views.login, name='login'),
    path('login/', views.login_view, name='login'),
    path('create-profile/', views.create_profile_view, name='create_profile'),
    path('profile/', views.profile, name='profile')
]
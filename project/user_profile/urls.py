from django.contrib import admin
from django.urls import path
from user_profile import views

urlpatterns = [
    path('', views.profile, name='profile'),
]
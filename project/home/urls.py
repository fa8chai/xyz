from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.main, name='main'),
    path('users/', views.overview, name='overview'),

]
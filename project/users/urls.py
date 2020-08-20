from django.contrib import admin
from django.urls import path
from users import views

urlpatterns = [
    path('login/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='signout'),
]
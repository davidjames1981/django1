from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.http import HttpResponse
from django.shortcuts import redirect
from . import views

app_name ='images'

urlpatterns = [
 
    path('', views.images_home, name='imageshome'), 
    path('<slug:image_id>/', views.show_image, name='show_image'), 
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
]
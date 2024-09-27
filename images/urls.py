from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.http import HttpResponse
from django.shortcuts import redirect
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.imageshome, name='imageshome'),
    path('imagehome/', views.imageshome, name='imagehome'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    
    # Redirect the root URL to the login page
    path('', lambda request: redirect('login')),
]

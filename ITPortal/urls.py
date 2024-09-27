"""
URL configuration for ITPortal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.http import HttpResponse
from django.shortcuts import redirect
from images import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('images/', include('images.urls')),  
#     path('onboarding/', include('onboarding.urls')),  
#     path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
#     path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
#     path('favicon.ico', lambda x: HttpResponse(status=204)),
    
#     # Redirect the root URL to the login page
#     path('', lambda request: redirect('login')),
# ]



urlpatterns = [
    path('admin/', admin.site.urls),
    path('images/', views.images_home, name='images_home'),
    path('images/<slug:image_id>/', views.show_image, name='show_image'), 
    path('onboarding/', include('onboarding.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]


from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [

    path('', views.onboarding_landing, name='onboarding_landing'),
    path('list/', views.onboarding_list, name='onboarding_list'),
    path('create/', views.onboarding_form, name='onboarding_create'),
    path('edit/<int:form_id>/', views.onboarding_form, name='onboarding_edit'),
    path('delete/<int:form_id>/', views.onboarding_delete, name='onboarding_delete'),
    path('hardware/<int:form_id>/', views.onboarding_hardware, name='onboarding_hardware'),  # Add this line
    path('applications/<int:form_id>', views.onboarding_applications, name='onboarding_applications'),  # URL for the application form
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout URL
]

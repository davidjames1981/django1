from django.contrib import admin
from .models import OnboardingForm,Department,Site,HardwareOption

class OnboardingFormAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'surname', 'manager')  # Add 'email'
    search_fields = ('first_name', 'surname', 'manager', 'department', 'email')  # Include 'email' in search fields
    list_filter = ('submitted', 'department', 'site', 'created_at')


# Registering the Department model in the admin
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Show only the name of the department in the admin list view
    search_fields = ('name',)  # Add search capability by department name

# Registering the Site model in the admin
class SiteAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Show only the name of the site in the admin list view
    search_fields = ('name',)  # Add search capability by site name

class HardwareOptionAdmin(admin.ModelAdmin):
    list_display = ['name']  # Display the name of the hardware option in the list
    search_fields = ['name']  # Add search functionality based on the name

# Registering the OnboardingForm, Department, and Site models
admin.site.register(OnboardingForm)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(HardwareOption, HardwareOptionAdmin)
admin.site.register(Site, SiteAdmin)




from django.db import models
from django.utils import timezone


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name  # Return the department name in string representation

class Site(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class HardwareOption(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
   
   
    
from django.db import models

class OnboardingForm(models.Model):

    # user creation fields
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    manager_email = models.EmailField()
    job_title = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)  # ForeignKey
    site = models.ForeignKey('Site', on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField()
    
    # Hardware fields
    need_hardware = models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')], default='N')
    need_wfh_hardware = models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')], default='N')
    hardware_option = models.ForeignKey('HardwareOption', on_delete=models.SET_NULL, null=True, blank=True)

    # Application fields
    invoice_automation = models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')], default='N')
    warranty_system = models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')], default='N')
    syspro_man = models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')], default='N')
    syspro_aft = models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')], default='N')
    syspro_int = models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')], default='N')

    submitted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.first_name} {self.surname}"


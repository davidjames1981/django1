from django import forms
from .models import OnboardingForm, HardwareOption,Site


class OnboardingFormInitial(forms.ModelForm):
    # first_name = forms.CharField(label='New Users First Name', required=True)
    # surname = forms.CharField(label='New Users Surname', required=True)
    # manager_email = forms.EmailField(label='New Users Line Managers Email', required=True)
    # job_title = forms.CharField(label='New Users Job Title', required=True)
    # department = forms.CharField(label='Department', required=True)
    # site = forms.ModelChoiceField(queryset=Site.objects.all(), label='Base site of the New user', required=True)
    # email = forms.EmailField(label='Submitters Email', required=True)

    class Meta:
        model = OnboardingForm
        fields = ['first_name', 'surname', 'manager_email', 'job_title', 'department', 'site', 'email']
        labels = {
            'first_name': 'New Users First Name',
            'surname': 'New Users Surname',
            'manager_email': 'New Users Line Managers Email',
            'job_title': 'New Users Job Title',
            'department': 'Department',
            'site': 'Base site of the New user',
            'email': 'Submitters Email',
        }


class OnboardingFormHardware(forms.ModelForm):
    need_hardware = forms.ChoiceField(choices=[('Y', 'Yes'), ('N', 'No')], label='Need Hardware')
    need_wfh_hardware = forms.ChoiceField(choices=[('Y', 'Yes'), ('N', 'No')], label='Need Work From Home Hardware')
    hardware_option = forms.ModelChoiceField(queryset=HardwareOption.objects.all(), required=False, label='Select Hardware')
    
    # Include the site field as a ModelChoiceField
    # site = forms.ModelChoiceField(queryset=Site.objects.all(), label='Site')

    class Meta:
        model = OnboardingForm
        fields = ['need_hardware', 'need_wfh_hardware', 'hardware_option' ]

    def clean(self):
        cleaned_data = super().clean()
        need_hardware = cleaned_data.get('need_hardware')
        hardware_option = cleaned_data.get('hardware_option')

        if need_hardware == 'Y' and not hardware_option:
            self.add_error('hardware_option', 'Please select a hardware option.')
        return cleaned_data

class OnboardingFormApplication(forms.ModelForm):
    invoice_automation = forms.ChoiceField(choices=[('Y', 'Yes'), ('N', 'No')], label='Invoice Automation')
    warranty_system = forms.ChoiceField(choices=[('Y', 'Yes'), ('N', 'No')], label='Warranty System')
    syspro_man = forms.ChoiceField(choices=[('Y', 'Yes'), ('N', 'No')], label='Syspro Man')
    syspro_aft = forms.ChoiceField(choices=[('Y', 'Yes'), ('N', 'No')], label='Syspro Aft')
    syspro_int = forms.ChoiceField(choices=[('Y', 'Yes'), ('N', 'No')], label='Syspro Int')
 
    class Meta:
        model = OnboardingForm
        fields = ['invoice_automation', 'warranty_system', 'syspro_man', 'syspro_aft', 'syspro_int' ]
    
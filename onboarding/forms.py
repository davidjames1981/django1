from django import forms
from .models import OnboardingForm, HardwareOption,Site


class OnboardingFormInitial(forms.ModelForm):
    class Meta:
        model = OnboardingForm
        fields = ['first_name', 'surname', 'manager_email', 'job_title', 'department', 'site', 'email']
        labels = {
            'first_name': 'New Users First Name',
            'surname': 'New Users Surname',
            'manager_email': 'New Users Line Managers Email',
            'job_title': 'New Users Job Title',
            'department': 'Base site of the New user',
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

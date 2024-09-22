from django import forms
from .models import OnboardingForm, HardwareOption,Site,Department


class OnboardingFormInitial(forms.ModelForm):
    first_name = forms.CharField(
        label='New Users First Name', 
        required=True, 
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter the first name',
            'required': 'required'
        })
    )
    surname = forms.CharField(
        label='New Users Surname', 
        required=True, 
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter the surname',
            'required': 'required'
        })
    )
    manager_email = forms.EmailField(
        label='New Users Line Managers Email', 
        required=True, 
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter the manager\'s email',
            'required': 'required'
        })
    )
    job_title = forms.CharField(
        label='New Users Job Title', 
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter the job title',
            'required': 'required'
        })
    )
    # This is the correct field for department dropdown
    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),  # Use ModelChoiceField with queryset
        label='Department',
        required=True,
        widget=forms.Select(attrs={'required': 'required'})
    )
    site = forms.ModelChoiceField(
        queryset=Site.objects.all(), 
        label='Base site of the New user', 
        required=True,
        widget=forms.Select(attrs={'required': 'required'})
    )
    email = forms.EmailField(
        label='Submitters Email', 
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter your email',
            'required': 'required'
        })
    )

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
    
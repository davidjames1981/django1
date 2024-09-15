from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import OnboardingFormInitial, OnboardingFormHardware
from .models import OnboardingForm


@login_required

def onboarding_form(request, form_id=None):
    form_instance = get_object_or_404(OnboardingForm, id=form_id) if form_id else None

    if request.method == 'POST':
        if 'save' in request.POST:
            form = OnboardingFormInitial(request.POST, instance=form_instance)
            if form.is_valid():
                form_instance = form.save(commit=False)
                form_instance.submitted = False
                form_instance.save()
                return redirect('onboarding_list')
        elif 'next' in request.POST:
            form = OnboardingFormInitial(request.POST, instance=form_instance)
            if form.is_valid():
                form_instance = form.save(commit=False)
                form_instance.save()
                return redirect('onboarding_hardware', form_instance.id)
    else:
        form = OnboardingFormInitial(instance=form_instance) if form_instance else OnboardingFormInitial()

    return render(request, 'onboarding/form.html', {'form': form})



@login_required
def onboarding_hardware(request, form_id):
    form_instance = get_object_or_404(OnboardingForm, id=form_id)
    if request.method == 'POST':
        form = OnboardingFormHardware(request.POST, instance=form_instance)
        
        print(request.POST)  # Debug: Print the POST data to see what is being submitted
        
        if form.is_valid():
            print(form.cleaned_data)  # Debug: Print cleaned data after validation
            form_instance = form.save(commit=False)

            if 'submit' in request.POST:
                form_instance.submitted = True

            form_instance.save()  # Save the form data to the database
            return redirect('onboarding_list')
        else:
            print("Form errors:", form.errors)  # Debug: Print form errors if invalid
    else:
        form = OnboardingFormHardware(instance=form_instance)

    return render(request, 'onboarding/hardware_form.html', {'form': form})


@login_required
def onboarding_delete(request, form_id):
    """
    View to delete an onboarding form.
    """
    form = get_object_or_404(OnboardingForm, id=form_id)
    form.delete()
    return redirect('onboarding_list')


@login_required
def onboarding_list(request):
    """
    View to list all unsubmitted onboarding forms.
    """
    forms = OnboardingForm.objects.filter(submitted=False)
    return render(request, 'onboarding/list.html', {'forms': forms})


@login_required
def onboarding_landing(request):
    """
    View for the onboarding landing page.
    """
    return render(request, 'onboarding/landing.html')

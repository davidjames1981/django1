from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import OnboardingFormInitial, OnboardingFormHardware,OnboardingFormApplication
from .models import OnboardingForm


@login_required
def onboarding_form(request, form_id=None):
    # Get the form instance if form_id is provided, otherwise initialize to None
    form_instance = get_object_or_404(OnboardingForm, id=form_id) if form_id else None

    if request.method == 'POST':
        # Save for later functionality
        if 'save' in request.POST:
            form = OnboardingFormInitial(request.POST, instance=form_instance)
            if form.is_valid():
                form_instance = form.save(commit=False)
                form_instance.submitted = False  # Mark as saved but not submitted
                form_instance.save()  # Save the form instance
                return redirect('onboarding_list')  # Redirect to onboarding list

        # Next button functionality - progress to the hardware form
        elif 'next' in request.POST:
            form = OnboardingFormInitial(request.POST, instance=form_instance)
            if form.is_valid():
                form_instance = form.save(commit=False)
                form_instance.save()  # Save the form instance
                return redirect('onboarding_hardware', form_instance.id)  # Redirect to hardware form

    else:
        # If GET request, initialize the form
        form = OnboardingFormInitial(instance=form_instance) if form_instance else OnboardingFormInitial()

    # Render the form template
    return render(request, 'onboarding/form.html', {'form': form})


@login_required
def onboarding_hardware(request, form_id):
    form_instance = get_object_or_404(OnboardingForm, id=form_id)
    
    if request.method == 'POST':
        form = OnboardingFormHardware(request.POST, instance=form_instance)

        if form.is_valid():
            form_instance = form.save(commit=False)  # Save form without committing to the database yet

            # Handling different button actions (save, submit, next)
            if 'submit' in request.POST:
                form_instance.submitted = True  # Mark the form as submitted
                form_instance.save()
                return redirect('onboarding_list')  # Redirect after submission

            elif 'next' in request.POST:
                form_instance.save()  # Save current form data
                return redirect('onboarding_applications', form_instance.id)  # Redirect to applications form

            elif 'save' in request.POST:
                form_instance.submitted = False  # Ensure it’s marked as saved but not submitted
                form_instance.save()
                return redirect('onboarding_list')  # Redirect to the list or another page after saving

        else:
            # Handle form errors
            print("Form errors:", form.errors)

    else:
        # GET request, load form with existing instance or empty form
        form = OnboardingFormHardware(instance=form_instance)

    return render(request, 'onboarding/hardware_form.html', {'form': form})





@login_required
def onboarding_applications(request, form_id):
    form_instance = get_object_or_404(OnboardingForm, id=form_id)


    if request.method == 'POST':
        form = OnboardingFormApplication(request.POST, instance=form_instance)
        if form.is_valid():
           
            # Handling different button actions (save, submit, next)
            if 'submit' in request.POST:
                form_instance.submitted = True  # Mark the form as submitted
                form_instance.save()
                return redirect('onboarding_list')  # Redirect after submission



            form.save()
            return redirect('onboarding_list')  # Or wherever you want to redirect after submission
    else:
        form = OnboardingFormApplication(instance=form_instance)

    return render(request, 'onboarding/applications_form.html', {'form': form})


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

import json
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import ContractorDetailsForm, BecomeContractorForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .utils import CONTRACTOR_SKILLS_CHOICES, CONTRACTOR_LOCATIONS_CHOICES

# Create your views here.
def contractor_profile(request, contractor_id):

    # Get the contractors UserProfile object. Automatically send 404 is the
    # profile does not exist, or if it is not a contractor profile. 
    contractor = get_object_or_404(UserProfile, pk=contractor_id, is_contractor=True)
    # Next check whether the user is viewing their own profile. This is useful
    # for permissinons as well as knowing what to render in the GET request.
    is_own_profile = contractor.user == request.user

    if request.method == 'POST':
        if not is_own_profile:
            return HttpResponse("You do not have permission to edit this profile")
        form = ContractorDetailsForm(request.POST, instance=contractor)
        if form.is_valid():
            form.save()
        else:
            print("ERROR ERROR ERROR")

    # Handle the GET request
    # Create the form for the UserProfile instance
    form = ContractorDetailsForm(instance=contractor)
    # Convert the availability dates to JSON for the template
    availability_json = json.dumps([str(date) for date in contractor.availability])
    # Contractors details packaged in a dictionary for the template
    contractor_pretty = {
        'username': contractor.user.username,
        
        'skills': contractor.skills,
        'locations': contractor.locations,
        'availability': contractor.availability,
        'bio': contractor.bio
    }
    return render(request, 'contractor/contractor_profile.html', {
        'contractor': contractor_pretty,
        'profile_form': form,
        'availability_json': availability_json,
        'is_own_profile': is_own_profile
    })


def split_string(string):
    if not string:
        return []
    return string.split(',')

@login_required
def become_contractor(request):
    profile = request.user.userprofile
    if profile.is_contractor:
        return HttpResponse("You are already a contractor")
    if request.method == 'POST':
        form_dict = {
            'skills': request.POST.getlist('skills'),
            'locations': request.POST.getlist('locations'),
            'availability': split_string(request.POST.get('availability', '')),
            'bio': request.POST.get('bio', '')
        }
        form = BecomeContractorForm(form_dict, instance=profile)
        if form.is_valid():
            print("Form is valid")
            contractor = form.save(commit=False)
            contractor.user = request.user
            contractor.is_contractor = True
            contractor.save()
            return HttpResponse("You are now a contractor")
        else:
            print("Form is invalid")
            print(form.errors)
    # End post request handling
    return render(request, 'contractor/become_contractor.html', {
        'skills': CONTRACTOR_SKILLS_CHOICES,
        'locations': CONTRACTOR_LOCATIONS_CHOICES
    })
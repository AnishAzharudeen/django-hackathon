import json
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import UserProfile, ContractorRating
from .forms import ContractorDetailsForm, ContractorRatingForm, BecomeContractorForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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
        'form': form,
        'skills': CONTRACTOR_SKILLS_CHOICES,
        'locations': CONTRACTOR_LOCATIONS_CHOICES
    })
    
    


def contractor_detail(request, user_profile_id):
    template= 'contractor/contractdetail.html'
    contractor = get_object_or_404(UserProfile, id=user_profile_id)
    ratings = ContractorRating.objects.filter(contractor=user_profile_id)
    if request.method == 'POST':
        form = ContractorRatingForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.creator = request.user
           
            review.contractor = contractor.user
            review.save()
            messages.add_message(
            request, messages.SUCCESS,
            'Review submitted and awaiting approval')
            return redirect('contractordetail' , user_id=user_id)
    else:
        form = ContractorRatingForm()
        availability_json = json.dumps([str(date) for date in contractor.availability])
        return render(request, 'contractor/contractordetail.html', {
            'contractor': contractor,
            'ratings': ratings, 
            'form': form, 
            'user': request.user,
            'availability_json': availability_json
        })


#  Edit and delete rating

def review_edit(request, slug, review_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = ContractorRating.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        review = get_object_or_404(ContractorRating, pk=review_id)
        review_form = ContractorRatingForm(data=request.POST, instance=review)

        if review_form.is_valid() and review.creator == request.user:
            review = review_form.save(commit=False)
            review.contractor = post
            review.approved = False
            review.save()
            messages.add_message(request, messages.SUCCESS, 'Review Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating Review!')

    return HttpResponseRedirect(reverse('contractordetail', args=[slug]))    


def review_delete(request, slug, review_id):
    """
    view to delete comment
    """
    queryset = ContractorRating.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    review = get_object_or_404(ContractorRating, pk=review_id)

    if review.creator == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own reviews!')

    return HttpResponseRedirect(reverse('contractordetail', args=[slug]))        



# creating views for contractor listview
from django.views import generic
from .models import UserProfile

from django.shortcuts import render

class ContractorList(generic.ListView):
    model = UserProfile
    queryset= UserProfile.objects.filter(is_contractor=True)
    template_name = 'contractor/contractor_list.html'
    context_object_name = 'contractors'
    paginate_by = 6

  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

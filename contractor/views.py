import json
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import UserProfile, ContractorRating
from .forms import ContractorDetailsForm, ContractorRatingForm, BecomeContractorForm, SearchForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .utils import CONTRACTOR_SKILLS_CHOICES, CONTRACTOR_LOCATIONS_CHOICES
# Create your views here.



def split_string(string):
    if not string:
        return []
    return string.split(',')

@login_required
def become_contractor(request):
    """
    The view function for the form to become a contractor.
    """
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
            return redirect('index')
        else:
            print("Form is invalid")
            print(form.errors)
    # End post request handling
    return render(request, 'contractor/become_contractor.html', {
        'skills': CONTRACTOR_SKILLS_CHOICES,
        'locations': CONTRACTOR_LOCATIONS_CHOICES
    })
    
@login_required
def edit_contractor_profile(request, user_profile_id):
    if request.user.userprofile.id != user_profile_id:
        return HttpResponse("You do not have permission to edit this profile")
    contractor = get_object_or_404(UserProfile, id=user_profile_id)
    if request.method == 'POST':
        form = ContractorDetailsForm(request.POST, instance=contractor)
        if form.is_valid():
            form.save()
            return redirect('contractordetail', user_profile_id=user_profile_id)
        else:
            print("ERROR ERROR ERROR")
    # End POST request handling
    print(contractor.skills)
    
    availability_json = json.dumps([str(date) for date in contractor.availability])
    return render(request, 'contractor/edit_contractor_profile.html', {
        'skills': CONTRACTOR_SKILLS_CHOICES,
        'locations': CONTRACTOR_LOCATIONS_CHOICES,
        'contractor': contractor,
        'availability_json': availability_json
    })


def contractor_detail(request, user_profile_id):
    """
    The view function for a contractor profile.
    """
    template= 'contractor/contractdetail.html'
    contractor = get_object_or_404(UserProfile, id=user_profile_id)
    ratings = ContractorRating.objects.filter(contractor=contractor.user)
    print(ratings)
    is_own_profile = contractor.user == request.user
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
            return redirect('contractordetail' , user_profile_id=user_profile_id)
    else:
        form = ContractorRatingForm()
        availability_json = json.dumps([str(date) for date in contractor.availability])
        return render(request, 'contractor/contractordetail.html', {
            'contractor': contractor,
            'ratings': ratings, 
            'form': form, 
            'user': request.user,
            'availability_json': availability_json,
            'is_own_profile': is_own_profile
        })


#  Edit and delete rating

def review_edit(request, user_profile_id, review_id):
    """
    view to edit comments
    """
    print(user_profile_id)
    print(review_id)
    if request.method == "POST":
        review = get_object_or_404(ContractorRating, pk=review_id)
        review_form = ContractorRatingForm(data=request.POST, instance=review)
        if review_form.is_valid() and review.creator == request.user:
            review = review_form.save()
            messages.add_message(request, messages.SUCCESS, 'Review Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating Review!')

    return HttpResponseRedirect(reverse('contractordetail', args=[user_profile_id]))    


def review_delete(request, user_profile_id, review_id):
    """
    view to delete comment
    """
    review = get_object_or_404(ContractorRating, pk=review_id)
    if review.creator == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own reviews!')

    return HttpResponseRedirect(reverse('contractordetail', args=[user_profile_id]))        



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


from django.views import generic
from django.db.models import Q

# Search List Page
class searchlist(generic.ListView):
    model = UserProfile
    template_name = 'contractor/search_listing.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = UserProfile.objects.filter(is_contractor=True)
        query = self.request.GET.get("q")
        skills = self.request.GET.getlist("skills")
        locations = self.request.GET.getlist("locations")
        availability = self.request.GET.getlist("availability")
        if query:
            query = query.lower()
            queryset = queryset.filter(
                Q(skills__icontains=query) | Q(locations__icontains=query)
            )
        if skills:
            queryset = queryset.filter(skills__overlap=skills)
        if locations:
            queryset = queryset.filter(locations__overlap=locations)
        
        if any(availability_date for availability_date in availability):
            queryset = queryset.filter(availability__overlap=availability)
        return queryset
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = SearchForm()
        context["skills_choices"] = CONTRACTOR_SKILLS_CHOICES
        context["locations_choices"] = CONTRACTOR_LOCATIONS_CHOICES
        context["selected_skills"] = self.request.GET.getlist("skills")
        context["selected_locations"] = self.request.GET.getlist("locations")
        context["availability_json"] = json.dumps([str(date) for date in self.request.GET.getlist("availability")])
        return context

    
# Advanced Search
@login_required
def advanced_search(request):
    """
    Allows users to make an advanced search
    """

    search_form = SearchForm()

    if request.method == "POST":
        search_form = SearchForm(request.POST)
        search_skills = request.POST.getlist('skills')
        search_area = request.POST.getlist('locations')
        queryset = UserProfile.objects.filter(skills__overlap=search_skills, locations__overlap=search_area)

        return render(
            request, 'contractors/search_listing.html',
            {"userprofile_list": queryset, 'search_form': search_form}
        )
    else:
        queryset = UserProfile.objects.filter(is_contractor=True)

    return render(
        request, 'contractors/search_listing.html',
        {"userprofile_list": queryset, 'search_form': search_form}
    )

from django import forms
from .models import UserProfile, ContractorRating, STAR_RATINGS
from .utils import CONTRACTOR_SKILLS_CHOICES, CONTRACTOR_LOCATIONS_CHOICES

class ContractorDetailsForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['skills', 'locations', 'availability']
        
    SKILLS_CHOICES = CONTRACTOR_SKILLS_CHOICES
    LOCATIONS_CHOICES = CONTRACTOR_LOCATIONS_CHOICES
    
    skills = forms.MultipleChoiceField(choices=SKILLS_CHOICES, widget=forms.CheckboxSelectMultiple())
    locations = forms.MultipleChoiceField(choices=LOCATIONS_CHOICES, widget=forms.CheckboxSelectMultiple())


class BecomeContractorForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['skills', 'locations', 'availability', 'bio']
        
    
    
class ContractorRatingForm(forms.ModelForm):
    class Meta:
        model = ContractorRating
        fields = ['rating', 'review']
        widgets = {
            'rating': forms.RadioSelect(choices=STAR_RATINGS),
            'review': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }

# Search Form
class SearchForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['skills', 'locations']
        widgets = {
            'skills': forms.CheckboxSelectMultiple(choices=CONTRACTOR_SKILLS_CHOICES),
            'locations': forms.CheckboxSelectMultiple(choices=CONTRACTOR_LOCATIONS_CHOICES),
        }
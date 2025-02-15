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

class ContractorRatingForm(forms.ModelForm):
    class Meta:
        model = ContractorRating
        fields = ['rating', 'content']
        widgets = {
            'rating': forms.RadioSelect(choices=STAR_RATINGS),
            'content': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }

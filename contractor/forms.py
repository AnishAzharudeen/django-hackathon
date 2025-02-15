from django import forms
from .models import UserProfile
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
        
    
    

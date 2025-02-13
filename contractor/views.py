import json
from django.shortcuts import render, get_object_or_404
from .models import ContractorProfile
from .forms import ContractorProfileForm

# Create your views here.
def contractor_profile(request, contractor_id):

    if request.method == 'POST':
        print(request.POST)
        contractor = get_object_or_404(ContractorProfile, pk=contractor_id)
        form = ContractorProfileForm(request.POST, instance=contractor)
        if form.is_valid():
            form.save()
        else:
            print("ERROR ERROR ERROR")

    contractor = get_object_or_404(ContractorProfile, pk=contractor_id)
    form = ContractorProfileForm(instance=contractor)
    availability_json = json.dumps([str(date) for date in contractor.availability])
    return render(request, 'contractor/contractor_profile.html', {
        'contractor': contractor,
        'profile_form': form,
        'availability_json': availability_json
    })
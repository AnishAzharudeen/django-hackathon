from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from contractor.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.db.models import Q


# Search List Page
class searchlist(generic.ListView):
    queryset = UserProfile.objects.filter(is_contractor=True)
    template_name = 'contractor/search_listing.html'
    paginate_by = 10

    def get_queryset(self):
        query = [self.request.GET.get("q")]

        if query != None:
            queryset = UserProfile.objects.filter(
                is_contractor=True and
                (Q(skills__icontains=query) |
                Q(locations__icontains=query))
            )
        else:
            queryset = UserProfile.objects.filter(is_contractor=True)
        
        return queryset


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    #path('<int:contractor_id>/', views.contractor_profile, name='contractor_profile'),
    path("<int:user_id>/", views.contractor_detail, name="contractordetail"), #Added by Anish
    path('become-contractor/', views.become_contractor, name='become_contractor'),
]
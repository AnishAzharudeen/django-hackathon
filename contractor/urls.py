from django.contrib import admin
from django.urls import path, include
from . import views, models

urlpatterns = [
    #path('<int:contractor_id>/', views.contractor_profile, name='contractor_profile'),
    # The detailed profile view for a single contractor
    path('<int:user_profile_id>/', views.contractor_detail, name="contractordetail"), #Added by Anish
    # The form to become a contractor
    path('become-contractor/', views.become_contractor, name='become_contractor'),
    # The form to edit a contractors profile
    path('<int:user_profile_id>/edit-profile/', views.edit_contractor_profile, name='edit_contractor_profile'),
    # Edit a given review
    path('<int:user_profile_id>/edit-review/<int:review_id>/', views.review_edit, name='review_edit'),
    # Delete a given review
    path('<int:user_profile_id>/delete-review/<int:review_id>/', views.review_delete, name='delete_review'),
    path('contractors/', views.ContractorList.as_view(), name='contractor_list'),
    path('search-list/', views.searchlist.as_view(), name="search_list"),
    path('advanced-search/', views.advanced_search, name="advanced_search"),
]

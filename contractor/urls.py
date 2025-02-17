from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    #path('<int:contractor_id>/', views.contractor_profile, name='contractor_profile'),
    path('<int:user_id>/', views.contractor_detail, name="contractordetail"), #Added by Anish
    path('become-contractor/', views.become_contractor, name='become_contractor'),
    path('contractor/<slug:slug>/edit_review/<int:review_id>/', views.review_edit, name='review_edit'),
    path('contractor/<int:review_id>/edit/', views.review_edit, name='edit_review'),
    path('review/<int:review_id>/delete/', views.review_delete, name='delete_review'),
    path('contractors/', views.ContractorList.as_view(), name='contractor_list'),
    path('search-list/', views.searchlist.as_view())
]

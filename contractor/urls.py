from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:contractor_id>/', views.contractor_profile, name='contractor_profile'),
    path('<slug:slug>/', views.post_detail, name='contractdetail'),
]

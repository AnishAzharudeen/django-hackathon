from django.contrib import admin
from .models import UserProfile, ContractorRating

# Register your models here.
@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'is_contractor', 'user', 'skills', 'locations', 'availability']
    
@admin.register(ContractorRating)
class ContractorRatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'creator', 'contractor', 'rating', 'created_at']
    list_filter = ['rating']
    search_fields = ['creator__username', 'contractor__username']

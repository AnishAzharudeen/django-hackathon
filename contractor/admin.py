from django.contrib import admin
from .models import ContractorProfile

# Register your models here.
@admin.register(ContractorProfile)
class ContractorAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'skills', 'locations', 'availability',]


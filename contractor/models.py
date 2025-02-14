from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.contrib.postgres.fields import ArrayField
from .utils import CONTRACTOR_SKILLS_CHOICES, CONTRACTOR_LOCATIONS_CHOICES
# Create your models here.


class UserProfile(models.Model):

    SKILLS_CHOICES = CONTRACTOR_SKILLS_CHOICES

    LOCATIONS_CHOICES = CONTRACTOR_LOCATIONS_CHOICES
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_contractor = models.BooleanField(default=False)
    profile_image = CloudinaryField('image', blank=True, null=True)
    skills = ArrayField(models.CharField(max_length=100, choices=SKILLS_CHOICES), blank=True, null=True)
    locations = ArrayField(models.CharField(max_length=100, choices=LOCATIONS_CHOICES), blank=True, null=True)
    availability = ArrayField(models.DateField(), blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username
    





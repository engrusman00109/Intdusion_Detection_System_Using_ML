# models.py

from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add fields for profile information
    bio = models.TextField(blank=True)
    # Add more fields as needed

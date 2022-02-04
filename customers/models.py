"""Customer models"""

# Django
from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    """Customer Class Model"""
    
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_picture = models.ImageField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    privacy_policy = models.BooleanField()

    def __str__(self):
        return self.first_name
 
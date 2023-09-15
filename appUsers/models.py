from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """
    Extend the django user model to add further details 
    for user profile, such as home address, phone number, 
    location (point geometry) where they live
    """
    ...
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    location = models.PointField(null=True, blank=True, srid=4326)

    class Meta:
        verbose_name = 'User'
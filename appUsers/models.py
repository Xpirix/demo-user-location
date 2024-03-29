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

class UserActivityLog(models.Model):
    """
    Model to log the user login/logout 
    activity by showing who and when on the admin page
    """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    action = models.CharField(max_length=10)  # 'login' or 'logout'
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.action} - {self.timestamp}'

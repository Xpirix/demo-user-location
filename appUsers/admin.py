from django.contrib.gis import admin
from .models import CustomUser

admin.site.register(CustomUser, admin.GISModelAdmin)

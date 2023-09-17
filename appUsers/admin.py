from django.contrib.gis import admin
from .models import CustomUser, UserActivityLog

# Register the custom user model using Gis model admin on the admin page
admin.site.register(CustomUser, admin.GISModelAdmin)
class UserActivityLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'timestamp')
    list_filter = ('action',)
    search_fields = ('user__username',)

# Register the CustomUser model using 
# UserActivityLogAdmin on the admin page
admin.site.register(UserActivityLog, UserActivityLogAdmin)

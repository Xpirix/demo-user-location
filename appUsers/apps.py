from django.apps import AppConfig


class AppusersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appUsers'

    def ready(self):
        """
        Fired when the appUsers is ready
        """
        import appUsers.signals
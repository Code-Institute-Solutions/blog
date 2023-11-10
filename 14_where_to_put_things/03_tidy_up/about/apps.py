from django.apps import AppConfig


class AboutConfig(AppConfig):
    """
    Provides primary key type for about app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'about'

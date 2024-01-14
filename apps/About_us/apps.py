from django.apps import AppConfig


class AboutUsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.About_us'

    def ready(self):
        import apps.About_us.signals

from django.apps import AppConfig


class DjangoMicroservicesAdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_microservices_admin'

    def ready(self):
        from . import settings

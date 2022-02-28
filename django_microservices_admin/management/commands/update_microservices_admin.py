import os
import sys
import shutil

from django.conf import settings
from django.core.management import BaseCommand, call_command

from django_microservices_admin.settings import SettingAttribute, MICROSERVICES_ADMIN_SETTINGS

BASE_DIR = getattr(settings, "BASE_DIR")


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        initial_stdout = sys.stdout
        for microservice_name, microservice_attrs in    MICROSERVICES_ADMIN_SETTINGS.items():
            tables = microservice_attrs[SettingAttribute.DATABASE_TABLES.value]

            if not os.path.exists(os.path.join(BASE_DIR, microservice_name)):
                call_command("startapp", microservice_name)

            models_file_path = os.path.join(BASE_DIR, microservice_name, 'models.py')
            if os.path.exists(models_file_path):
                shutil.move(
                    os.path.join(models_file_path),
                    os.path.join(BASE_DIR, microservice_name, 'models.old.py')
                )

            with open(models_file_path, 'w') as sys.stdout:
                call_command("inspectdb", tables, database=microservice_name)
                sys.stdout = initial_stdout

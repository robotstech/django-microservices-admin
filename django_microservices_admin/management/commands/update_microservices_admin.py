import os
import shutil

from django.conf import settings
from django.core.management import BaseCommand
from django.core.management.commands import startapp, inspectdb

from django_microservices_admin.settings import SettingAttribute

BASE_DIR = getattr(settings, "BASE_DIR")
MICROSERVICES_ADMIN_SETTINGS = getattr(settings, "MICROSERVICES_ADMIN")


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for microservice_name, microservice_attrs in MICROSERVICES_ADMIN_SETTINGS.items():
            tables = microservice_attrs[SettingAttribute.DATABASE_TABLES.value]

            if not os.path.exists(os.path.join(BASE_DIR, microservice_name)):
                startapp.Command().handle(name=microservice_name)

            if os.path.exists(os.path.join(BASE_DIR, microservice_name, 'models.py')):
                shutil.move(
                    os.path.join(BASE_DIR, microservice_name, 'models.py'),
                    os.path.join(BASE_DIR, microservice_name, 'models.old.py')
                )

            inspectdb.Command().handle(table=tables, database=microservice_name)

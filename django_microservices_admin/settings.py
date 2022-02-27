from enum import Enum

import dj_database_url
from django.conf import settings

DATABASES = getattr(settings, "databases", None)
MICROSERVICES_ADMIN_SETTINGS = getattr(settings, "MICROSERVICES_ADMIN", None)

print("hello", MICROSERVICES_ADMIN_SETTINGS)
if not MICROSERVICES_ADMIN_SETTINGS:
    raise AttributeError("MICROSERVICES_ADMIN must be declared in settings")


class SettingAttribute(Enum):
    DATABASE_URL = "DATABASE_URL"
    DATABASE_TABLES = "DATABASE_TABLES"


for microservice_name, microservice_attrs in MICROSERVICES_ADMIN_SETTINGS:
    DATABASES[microservice_name] = dj_database_url.parse(microservice_attrs[SettingAttribute.DATABASE_URL])


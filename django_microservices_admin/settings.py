from enum import Enum

import dj_database_url

MICROSERVICES_ADMIN_SETTINGS = None


class SettingAttribute(Enum):
    DATABASE_URL = "DATABASE_URL"
    DATABASE_TABLES = "DATABASE_TABLES"


def update(user_settings: dict, microservices_admin_settings: dict):
    global MICROSERVICES_ADMIN_SETTINGS
    MICROSERVICES_ADMIN_SETTINGS = microservices_admin_settings

    for microservice_name, microservice_attrs in microservices_admin_settings.items():
        user_settings['DATABASES'][microservice_name] = dj_database_url.parse(
            microservice_attrs[SettingAttribute.DATABASE_URL.value]
        )

    user_settings['DATABASE_ROUTERS'] = ['django_microservices_admin.routers.AuthRouter']

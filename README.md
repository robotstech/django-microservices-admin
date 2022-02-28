# django-microservices-admin
![main workflow](https://github.com/robotech/django-microservices-admin/actions/workflows/main.yml/badge.svg) <br>
This project make it possible to use Django's Admin Interface to administrate your microservices. Sample project [here](https://github.com/robotstech/django-microservices/tree/main/message_boards_admin)


## Quick Start Instructions
### Prerequisites

1. Django Project for the microservices admin
2. Microservices with individual databases

### Tools and Resources
1. Python 3.8+ [link](https://www.python.org/downloads/release/python-387/)
2. Virtualenv

### Installation
1. Install with pip <br /> from pypi *(upcoming)*  
 ``` shell
 pip install django-microservices-admin
 ```
 from git  
 ```
 pip install git+https://github.com/robotstech/django-microservices-admin.git
 ```
2. install database driver(s). <br /> 
 - install for postgres driver: 
 ``` shell 
 pip install psycopg2-binary>=2.9.3
 ```
 - install for mysql driver: 
 ``` shell 
 pip install mysqlclient>=2.1.0
 ```

 - here are some supported drivers for django click [here](https://docs.djangoproject.com/en/4.0/ref/databases/
 ) to see.

| Database   |    Driver   |
| --------   | --------  |
| Postgres | [pycopg2](https://pypi.org/project/psycopg2/)|
| Mysql  | [mysqlclient](https://pypi.org/project/mysqlclient/)|


### Set up a (new) Microservice app admin
This is a setup for a simple microservice case, you can follow the same step to add more microservices
1. Add the following to the bottom of your `settings.py` to add a microservice database. All tables will be registered if `"DATABASE_TABLES": []`
```python
import django_microservices_admin.settings
django_microservices_admin.settings.update(
    locals(),
    {
        '{MICROSERVICE_NAME}': {
            "DATABASE_URL": "postgresql://postgres:postgres@localhost:5432/message_boards", # replace this with the right url
            "DATABASE_TABLES": ["list", "of", "table", "names"]
        }
    }
)
```
2. Create an app to represent the microservice. A `models.py` file will be created containing classes (django models) representing the database tables in your microservice db. Make sure to edit and format it accordingly(see [here](https://docs.djangoproject.com/en/4.0/howto/legacy-databases/) and [here](https://docs.djangoproject.com/en/4.0/ref/django-admin/#django-admin-inspectdb) for more info). __Note__: When the command is executed again a `models.old.py` is created containing the previous model.py and a new `models.py` is created containing a more recent but not formatted version. __This will not affect your existing microservice db schema in any way__
```shell 
python manage.py update_microservices_admin
```
3. Include microservice in installed apps
```python
INSTALLED_APPS = [
    ...,
    '{MICROSERVICE_NAME}',
]
```
4. Include microservice model(s) in `{MICROSERVICE_NAME}/admin.py`
```python
from django.contrib import admin
from {MICROSERVICE_NAME}.models import SomeModel

admin.site.register(SomeModel)
```
5. Create Super User.
```shell
python manage.py createsuperuser --username admin
```
6. Visit [admin](http://127.0.0.1:8000/admin/)

### Update (existing) Microservice app admin
Run the command
```shell 
python manage.py update_microservices_admin
```


## Usage/In-depth API Documentation.
See [DOCUMENTATION.md](DOCUMENTATION.md)

## Contributing
See [CONTRIBUTION.md](CONTRIBUTION.md)

## Code of conducts
See [Code of Conducts](CODE_OF_CONDUCT.md)

## Authors/Contributors
See list of [contributors](https://github.com/robotstech/django-microservices-admin/graphs/contributors) 
who contributed to this project

## Security Contact
Please disclose any security-related issues or vulnerabilities by emailing 
[contact's email](mailto:tech@robotslimited.com), instead of using the public issue tracker. 
See [SECURITY.md](SECURITY.md) for more information.

## License
See list of [LICENSE](LICENSE) 
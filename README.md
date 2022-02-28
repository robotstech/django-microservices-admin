# django-microservices-admin
![main workflow](https://github.com/iamr0b0tx/json-api/actions/workflows/main.yml/badge.svg) <br>
This project make it possible to use Django's Admin Interface to administrate your microservices.


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


### Setup
This is a setup for a simple microservice case, you can follow the same step with other microservices
1. Add a microservice database as follows:
   ``` python
   
   MICROSERVICES_ADMIN = {
       '{MICROSERVICE_NAME}': {
            DATABASE_URL: '{MICROSERVICE_DATABASE_URL}',
            DATABASE_TABLES": ['list', 'of', 'table', 'names']
       },
   }
   ```
1. Create an app to represent the microservice
   ``` shell 
   py manage.py update_microservices_admin
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
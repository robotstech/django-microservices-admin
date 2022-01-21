# django-microservices-admin
![main workflow](https://github.com/iamr0b0tx/json-api/actions/workflows/main.yml/badge.svg) <br>
This project make it possible to use Django's Admin Interface to administrate your microservices.


## Quick Start Instructions
### Prerequisites
### Tools and Resources
1. Python 3.8+ [link](https://www.python.org/downloads/release/python-387/)
2. Virtualenv

### Installation
Make sure to download/clone this repository and navigate to the folder in your terminal. Now follow the instructions 
below

1. Create the virtual environment.
```shell script
virtualenv /path/to/venv --python=/path/to/python3
```
You can find out the path to your `python3` interpreter with the command `which python3`.

1. Set up `.env` file by duplicating the `.example.env` file(and editing if required).

1. Activate the environment and install dependencies.
    - #### Linux
    ```shell script
    source /path/to/venv/bin/activate
    pip install -r requirements.txt
    ```

    - #### Windows
    ```cmd
    ./path/to/venv/bin/activate
    pip install -r requirements.txt
    ```
1. Launch the app
    ```shell script
    python manage.py runserver
   

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
# InstaEats

This Project is if sudofire

### About
This project is based on django(v2.2)/python3.7.2

### Setup
* make a virtual environment using command "virtualenv --python=/usr/bin/python3.7.2 path/to/new/virtualenv"

* navigate to virtual environment directory and activate virtual environment using command "source bin/activate"

* install requirements.txt using command "pip3 install -r requirements.txt"

* setup postgresql database using project settings.py file

* navigate to project directory

* start server using command "python3 manage.py runserver"

## local settings
You can override variable in `settings.py` by using `local.py` in `project/_settings` directory for local dev environments. local settings can have following settings.

```

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'if_sudofire',
        'USER': 'if_sudofire',
        'PASSWORD': 'if_sudofire',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'ATOMIC_REQUEST': True,
    }
}

ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

```
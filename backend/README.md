# backend

This template should help get you started developing Django and Django REST Framework.

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/)

## Project Setup

```sh
python -m venv venv
Set-ExecutionPolicy Unrestricted -Scope Process # for Windows
venv\Scripts\activate
pip install -r requirements.txt
```

### Run and Hot-Reload for Development

```sh
py backend_api/manage.py collectstatic
py backend_api/manage.py runserver
```

### Run and Hot-Reload for production
Make sure that you have set up an environment variable `DJANGO_DEBUG = False` .

You can also specify `SECRET_KEY = <your-key>` as environment variable. 

```sh
py backend_api/manage.py collectstatic
py backend_api/manage.py runserver
```
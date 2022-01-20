# Django  

## Creating a project

```bash
$ django-admin startproject mysite
```

생성된 파일을 살펴보면: 

```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

- `manage.py` : A command-line utility that lets you interact with this Django project in various ways.
- `mysite/__init__.py` : An empty file that tells Python that this directory should be considered a Python package.
- `mysite/settings.py` : Settings/configuration for this Django project.
- `mysite/urls.py` : The URL declarations for this Django project; a “table of contents” of your Django-powered site.
- `mysite/asgi.py` : An entry-point for ASGI-compatible web servers to serve your project.
- `mysite/wsgi.py` : An entry-point for WSGI-compatible web servers to serve your project.



## Running the development server

```bash
$ python manage.py runserver
```

By default, the `runserver` command starts the development server on the internal IP at port 8000.

If you want to change the server’s port, pass it as a command-line argument. For instance, this command starts the server on port 8080:

```bash
$ python manage.py runserver 8080
```



## Creating an app

### Projects vs. apps

An app is a web application that does something – e.g., a blog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.



## Activating models

After creating an app, we need to tell our project that the app is installed. To include the app in our project, we need to add a reference to its configuration class in the `INSTALLED_APPS` setting.

For example, if we made a `polls` app:

```python
INSTALLED_APPS = [
    'polls.apps.PollsConfig',  # [App name].apps.[App name]Config
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

Then let's run a command:

```bash
$ python manage.py makemigrations polls
```

`makemigrations` tell Django that you've made some changes to models and that you'd like the changes to be stored as a migration. Migrations are how Django stores changes to your models.

Now, run `migrate` to create those model tables in your database:

```bash
$ python manage.py migrate
```


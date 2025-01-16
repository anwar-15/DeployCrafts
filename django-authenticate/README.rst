===================
django-authenticate
===================

django-authenticate v0.1 is a basic app that allows user to register, login and logout.
It accepts username emailId for registration, login with username.
Detailed information is in the docs

Quick Start
-------------

1. Add "authenticate" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        'authenticate.apps.AppConfig',
    ]

2. Include the authenticate URLconf in your project urls.py like this::

    path("authenticate/", include("authenticate.urls")),

3. Run ``python manage.py makemigrations`` to create migrations for models
4. Run ``python manage.py migrate`` to create the models.

5. Start the development server by running ``py manage.py runsrver`` and visit the admin @ ``/admin/`` url to administer users.

6. Visit the ``/authenticate/register`` url to register new users.

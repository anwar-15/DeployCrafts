==========================
django-authenticate v1.0.0
==========================

django-authenticate v1.0.0 is an authentication app that allows user to register, login and logout.
It accepts username emailId for registration, login with username and password.

Includes :
 * Email verification of registered users
 * Dynamic Creation of user's profile for verified users
 * Admin Site Integration

Detailed information is in the docs

Quick Start
-------------

1. Add "authenticate" and "accounts" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        'authenticate.apps.AuthenticateConfig',
        'accounts.apps.AccountsConfig',
    ]

2. Include the authenticate URLconf in your project urls.py like this::

    path("authenticate/", include("authenticate.urls")),

3. In settings.py add::

    AUTH_USER_MODEL = 'authenticate.Registrar'

4. In settings.py add::

    LOGIN_URL = 'authenticate:login'

#To setup email-sender. For example gmail server:
5. In Settings.py add::

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = "your-mail-id@gmail.com"
    EMAIL_HOST_PASSWORD = "app-password"

6. Run ``python manage.py makemigrations`` to create migrations for models

7. Run ``python manage.py migrate`` to create the models.

8. Run ``python manage.py createsuperuser`` to create admin user

9. Start the development server by running ``py manage.py runserver`` and visit the admin @ ``/admin/`` url to administer users.

10. Visit the ``/authenticate/register`` url to register new users.
11. Visit the ``/authenticate/login`` url to login users.


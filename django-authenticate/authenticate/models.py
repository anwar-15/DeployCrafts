from django.contrib.auth.models import AbstractUser
from django.contrib import admin

# Create your models here.
class Registrar(AbstractUser):
    REQUIRED_FIELDS = ["email", 'first_name', 'last_name']

admin.site.register(Registrar)
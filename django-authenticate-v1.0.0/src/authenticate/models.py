from django.contrib.auth.models import AbstractUser, UserManager
#from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Registrar(AbstractUser):

    email = models.EmailField(_("email address"), blank=True, unique=True)
    is_verified = models.BooleanField(
        _("Email Verified"),
        default=False,
        help_text=_("Designates whether the user has verified email address."),
    )

    is_active = models.BooleanField(
        _("active"),
        default=False,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    objects = UserManager()
    REQUIRED_FIELDS = ["email", 'first_name', 'last_name']

#admin.site.register(Registrar)
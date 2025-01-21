from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import UserManager
# Create your models here.

RegModel = get_user_model()

class Profile(models.Model):

    user = models.OneToOneField(RegModel, on_delete=models.CASCADE, related_name='profile')
    is_verified = models.BooleanField(default=False)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='profile-pic/', blank=True, null=True)

    objects = UserManager()

    def __str__(self):
        return f"{self.user.username}'s Profile"



'''from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

RegModel = get_user_model()

class UsernameOrEmailBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):

        try:
            if
            RegModel.object.get()
        except RegModel.DoesNotExist:
            return None

        if user.check_password(password) and self.user_can_authenticate(user):
            return user

        return None'''
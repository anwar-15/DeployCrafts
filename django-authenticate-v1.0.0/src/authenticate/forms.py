from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.forms import AuthenticationForm

RegModel = get_user_model()

class RegistrationForm(forms.models.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    class Meta():
        model = RegModel
        fields = ['email', 'username','password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        email = cleaned_data.get('email')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        '''if RegModel.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("This email is already in use.")'''

        return cleaned_data

    #TODO: To beresolved in v.03
    '''def confirm_register_allowed(self, user):  

        if user.is_verified:        
            raise ValidationError(
                "Email is already Verified. Account with this email already Exists",
                code="verified",
            )'''

class LoginForm(AuthenticationForm):

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        #Validating Authentications
        if username is not None and password:
            try:
                self.user = RegModel.objects.get(username=username)
            except RegModel.DoesNotExist:
                raise ValidationError("User is not Registered!!")

            self.user_cache = authenticate(
                self.request, username=username, password=password
            )
            #Controls whether the given user is active or not.
            if self.user_cache is None:
                if  not self.user.is_active:
                    self.confirm_login_allowed(self.user)
                else:
                    raise self.get_invalid_login_error()

        return self.cleaned_data

    def confirm_login_allowed(self, user):
        """
        Controls whether the given User may log in. This is a policy setting,
        independent of end-user authentication. This default behavior is to
        allow login by active users, and reject login by inactive users.

        If the given user cannot log in, this method should raise a
        ``ValidationError``.

        If the given user may log in, this method should return None.
        """
        if not user.is_active:
            raise ValidationError(
                self.error_messages["inactive"],
                code="inactive",
            )

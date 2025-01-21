from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django import forms
# Register your models here.
RegModel = get_user_model()

class AdminUserChangeForm(forms.ModelForm):
    class Meta:
        model = RegModel
        fields = '__all__'

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if RegModel.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("This email is already in use.")
        return email

class AdminSite(UserAdmin):

    form = AdminUserChangeForm
    # Customize the fields displayed in the admin interface
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_verified', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Specify the fields displayed in the list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_verified', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

admin.site.register(RegModel, AdminSite)
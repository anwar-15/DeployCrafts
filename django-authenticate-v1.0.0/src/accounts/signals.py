from django.dispatch import receiver
from src.authenticate.signals import user_created_signal
from django.apps import apps

profile = apps.get_model('accounts', 'Profile')

@receiver(user_created_signal)
def create_user_profile(sender, **kwargs):

    instance = kwargs.get('instance')
    if instance:
        if not hasattr(instance, 'profile'):
            profile.objects.create(user=instance)





from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Get the user model
User = settings.AUTH_USER_MODEL

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
    Automatically create a DRF token whenever a new user is created.
    """
    if created:
        Token.objects.create(user=instance)
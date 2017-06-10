from django.contrib.auth.models import User
from django.db import models
from IsyncWeb import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Notes(models.Model):
    title=models.TextField(max_length=30)
    text=models.TextField(max_length=500)
    username=models.TextField(max_length=15)
    date = models.DateTimeField(auto_now_add=True)


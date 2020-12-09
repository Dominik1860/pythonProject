from .enums import *
from datetime import datetime
from django.db import models
from django.contrib.auth import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """
    Profile model class
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='User')
    bio = models.TextField(max_length=255, null=True, blank=True)
    mugshot = models.ImageField(upload_to='static/imgs/profile/', default='static/imgs/dummy_profile.jpg')
    birthdate = models.DateField(null=True, blank=True)
    telephone = models.CharField(null=True, blank=True, max_length=12)
    friends = models.ManyToManyField('self', symmetrical=True)

    # https://docs.djangoproject.com/en/3.0/ref/models/fields/#django.db.models.ManyToManyField

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        """
        Trigger that creates Profile when djangos User is created
        """
        if created:
            Profile.objects.create(user=instance)

    def __str__(self):
        return self.user.get_username()
from .enums import *
from datetime import datetime
from django.db import models
from django.contrib.auth import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# class TestModel(models.Model):
#     mugshot = models.ImageField(upload_to='static/imgs/')

class Profile(models.Model):
    """
    Profile model class
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    bio = models.TextField(max_length=255, null=True, blank=True)
    mugshot = models.ImageField(upload_to='static/imgs/profile/', default='static/imgs/dummy_avatar.jpg')
    birthdate = models.DateField(null=True, blank=True)
    telephone = models.CharField(null=True, blank=True, max_length=12)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        """
        Trigger that creates Profile when djangos User is created
        """
        if created:
            Profile.objects.create(user=instance)

    def __str__(self):
        return self.user.get_username()

class FriendRequest(models.Model):
    """
    Model class for a friend request from a particular user (1:1) to another particular user (1:1)
    """

    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='to_user', on_delete=models.CASCADE)
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='from_user', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "From {}, to {}".format(self.from_user.username, self.to_user.username)

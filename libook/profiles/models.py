from .enums import *
from datetime import datetime
from django.db import models
from django.contrib.auth import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    """
    Model class for an profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField(null=True, blank=True)
    telephone = models.CharField(null=True, blank=True, max_length=12)
    privacy_settings = models.TextField(choices=AccessTypes.choices(), default=AccessTypes.PUBLIC)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        """
        Trigger for creating Profile with django's User
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


class Reaction(models.Model):
    """
    Model class for a reaction from a particular user (1:1) to a particular post (1:1)
    """
    user_id = models.ForeignKey('profiles.profile', on_delete=models.CASCADE)
    post_id = models.ForeignKey('posts.post', on_delete=models.CASCADE)
    # reaction_type = models.TextField(choices=ReactionTypes.choices(), default=ReactionTypes.LIKE)

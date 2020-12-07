from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import settings
from profiles.models import Profile
from posts.models import Post


class Event(models.Model):
    """
    Event model class
    """
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, default=None, null=True, blank=True)
    feed = models.ManyToManyField('posts.post', on_delete=models.CASCADE, default=None, null=True, blank=True)
    # feed = models.ManyToManyField('self', symmetrical=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='static/imgs/profile/', default='static/imgs/dummy_avatar.jpg')


class InvitationRequest(models.Model):
    """
    Model class for an invitation request from a particular user (1:1) to an particular event (1:1)
    """

    to_event = models.ForeignKey('.event', related_name='to_event', on_delete=models.CASCADE)
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='from_user', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "From {}, to {}".format(self.from_user.username, self.to_event.name)

from django.db import models
from django.conf import settings
from django.contrib.auth import settings
from datetime import datetime


class Event(models.Model):
    """
    Model class for an event from a particular user (1:1).
    """
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="event_members", default=None, blank=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(max_length=255, null=True, blank=True)
    when = models.DateTimeField(null=False, blank=False, default=datetime.now)
    where = models.CharField(max_length=255, null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} ({self.when}, {self.where})'


class EventInvitationRequest(models.Model):
    """
    Model class for an invitation request from a particular user (1:1) to an particular event (1:1)
    """

    to_event = models.ForeignKey('event', on_delete=models.CASCADE)
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "From {}, to {}".format(self.from_user.username, self.to_event.name)

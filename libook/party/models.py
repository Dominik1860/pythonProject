from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import settings
from profiles.models import Profile
from posts.models import Post


class Party(models.Model):
    """
    Model class for a party from a particular user (1:1).
    """
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="party_members", default=None, blank=True)
    bio = models.TextField(max_length=255, null=True, blank=True)
    genre = models.TextField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='static/imgs/party/', default='static/imgs/dummy_party.jpg')


class PartyInvitationRequest(models.Model):
    """
    Model class for an invitation request from a particular user (1:1) to a particular party (1:1).
    """
    to_party = models.ForeignKey('party', on_delete=models.CASCADE)
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "From {}, to {}".format(self.from_user.username, self.to_party.partyname)

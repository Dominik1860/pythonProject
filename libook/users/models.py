from django.db import models
from datetime import datetime
from django.utils import timezone
from .enums import *
from autoslug import AutoSlugField
# pip install django-autoslug

class User(models.Model):
    """
    Model class for an user
    """

    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    email = models.EmailField()
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    birthdate = models.DateField()
    telephone = models.CharField(max_length=12)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    # need to provide a default image
    bio = models.CharField(max_length=255, blank=True)
    privacy_settings = models.TextField(choices=AccessTypes.choices(), default=AccessTypes.PUBLIC)

    def __str__(self):
        return str(self.user.username)

    def get_absolute_url(self):
        return "/users/{}".format(self.slug)

    def getAge(self):
        """
        Calculates the age of the user
        """
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        return age if (today < datetime.date(today.year, self.birthdate.month, self.birthdate.day)) else age - 1

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
    user_id = models.ForeignKey('users.user', on_delete=models.CASCADE)
    post_id = models.ForeignKey('posts.post', on_delete=models.CASCADE)
    # reaction_type = models.TextField(choices=ReactionTypes.choices(), default=ReactionTypes.LIKE)

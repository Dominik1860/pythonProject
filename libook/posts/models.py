from django.db import models
from .enums import *


class Post(models.Model):
    """
    Model class for a post from a particular user (1:1)
    """
    name = models.CharField(max_length=255)
    description = models.TextField(null=False, blank=False, max_length=255)
    # content_url = models.ImageField()
    number_of_likes = models.PositiveIntegerField(default=0)
    tagged_user_id = models.ForeignKey('users.user', on_delete=models.RESTRICT, default=None, null=True)
    post_type = models.TextField(choices=PostTypes.choices(), default=PostTypes.TEXT)
    privacy_settings = models.TextField(choices=AccessTypes.choices(), default=AccessTypes.PRIVATE)

class Comment(models.Model):
    """
    Model class for a comment from a particular user (1:1) to a particular post (1:1)
    """
    user_id = models.ForeignKey('users.user', on_delete=models.CASCADE)
    post_id = models.ForeignKey('posts.post', on_delete=models.CASCADE)
    content = models.TextField(null=False, blank=False, max_length=255)

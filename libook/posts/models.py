from django.db import models
from django.conf import settings
from profiles.models import Profile


class Post(models.Model):
    """
    Model class for a post from a particular user (1:1).
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=False, blank=False, max_length=255)
    image = models.ImageField(upload_to='static/imgs/posts/', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " (from " + self.user.username + ")"


class Comment(models.Model):
    """
    Model class for a comment from a particular user (1:1) to a particular post (1:1).
    """
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # https://stackoverflow.com/questions/34305805/django-foreignkeyuser-in-models
    post_id = models.ForeignKey('posts.post', on_delete=models.CASCADE)
    content = models.TextField(null=False, blank=False, max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    """
    Model class for a like from a particular user (1:1) to a particular post (1:1).
    """
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # https: // stackoverflow.com / questions / 34305805 / django - foreignkeyuser - in -models
    post_id = models.ForeignKey('posts.post', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

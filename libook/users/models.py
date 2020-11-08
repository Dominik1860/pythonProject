from django.db import models
from datetime import datetime
from .enums import *

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
    privacy_settings = models.TextField(choices=AccessTypes.choices(), default=AccessTypes.PUBLIC)

    def getAge(self):
        """
        Calculates the age of the user
        """
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        return age if (today < datetime.date(today.year, self.birthdate.month, self.birthdate.day)) else age - 1


class Reaction(models.Model):
    """
    Model class for a reaction from a particular user (1:1) to a particular post (1:1)
    """
    user_id = models.ForeignKey('user', on_delete=models.CASCADE)
    post_id = models.ForeignKey('post', on_delete=models.CASCADE)
    # reaction_type = models.TextField(choices=ReactionTypes.choices(), default=ReactionTypes.LIKE)

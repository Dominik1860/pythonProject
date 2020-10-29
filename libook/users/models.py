from django.db import models
from datetime import datetime
from enum import IntEnum


class AccessTypes(IntEnum):
    """
    Enumeration for privacy definition of post or feed
    """
    PRIVATE = 0
    PUBLIC = 1

    @classmethod
    def choices(cls):
        return[(key.value, key.name) for key in cls]


# class PostTypeEnum(models.IntegerField):
#     """
#     Enumeration for defining the content type of a post
#     """
#     TEXT = 0, ('Text')
#     IMAGE = 1, ('Image')
#     VIDEO = 2, ('Video')

class ReactionTypeEnum(IntEnum):
    """
    Enumeration for defining the reaction to a post
    """
    LIKE = 0, ('Like')
    SHARE = 1, ('Share')


class User(models.Model):
    """
    Model class for an user
    """

    # def __init__(self, id, email, username, password, name, surname, birthdate, telephone, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.id = id
    #     self.email = email
    #     self.username = username
    #     self.password = password
    #     self.name = name
    #     self.surname = surname
    #     self.birthdate = birthdate
    #     self.telephone = telephone

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


class Comment(models.Model):
    """
    Model class for a comment from a particular user (1:1) to a particular post (1:1)
    """
    user_id = models.ForeignKey('user', on_delete=models.CASCADE)
    post_id = models.ForeignKey('post', on_delete=models.CASCADE)
    content = models.TextField(null=False, blank=False, max_length=255)

    # def __init__(self, id, user_id, post_id, content, *args, **kwargs):
    #    super().__init__(*args, **kwargs)
    #    self.id = id
    #    self.user_id = user_id
    #    self.post_id = post_id
    #    self.content = content

class Post (models.Model):
    """
    Model class for a post from a particular user (1:1)
    """
    name = models.CharField(max_length=15)
    description = models.TextField(null=False, blank=False, max_length=255)
    # content_url = models.
    number_of_likes = models.DecimalField()
    tagged_user_id = models.ForeignKey('user', on_delete=models.CASCADE)
    post_type_id = models.ForeignKey('PostTypeEnum', on_delete=models.CASCADE)
    privacy_settings = models.TextField(choices=AccessTypes.choices(), default=AccessTypes.PRIVATE)


class Reaction (models.Model):
    """
    Model class for a reaction from a particular user (1:1) to a particular post (1:1)
    """
    post_id = models.ForeignKey('post', on_delete=models.CASCADE)
    reaction_type_id = models.ForeignKey('ReactionTypeEnum', on_delete=models.CASCADE)
from django.db import models
from enum import Enum

# Create your models here.

class User(models.Model):
    id = models.DecimalField()
    email = models.EmailField()
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    birthdate = models.DateField()
    telephone = models.DecimalField(max_digits=12)
    test_attr2 = models.IntegerField()
    # User Model correct implemented?

    def __init__(self, id, email, username, password, name, surname, birthdate, telephone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = id
        self.email = email
        self.username = username
        self.password = password
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.telephone = telephone

        def age(self):
            today = datetime.date.today()
            age = today.year - self.birthdate.year

            if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
                age -= 1

            return age
        # calculates the age of user


class Comment(models.Model):
    id = models.DecimalField()
    # user_id
    # post_id
    content = models.TextField(max_length=120)

    def __init__(self, id, user_id, post_id, content, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = id
        self.user_id = user_id
        self.post_id = post_id
        self.content = content


class Feed(models.Model):
    id = models.DecimalField()
    # user_id
    # post_id
    access_type = models.TextField(max_length=120)

    def __init__(self, id, user_id, post_id, content, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = id
        self.user_id = user_id
        self.post_id = post_id
        self.access_type = access_type

class Access_Type(Enum):
    private = 1
    public = 2
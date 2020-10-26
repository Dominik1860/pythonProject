from django.contrib import admin

from .models import User, Comment, Feed, Access_Type


# Register your models here.

admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Feed)
admin.site.register(Access_Type)

from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .models import Post
from . import forms


def detail(request, **kwargs):
    post_id = kwargs['id']
    # post = Post.objects.get(pk=post_id)

    context = {
        'id' : post_id,
        'test': 'test',
        'test_number': 1
    }

    return render(request, 'post/detail.html', context)



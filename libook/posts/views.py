from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .models import Post


class IndexView(View):
    def get(self):
        return HttpResponse("<h1></h1>")

    def post(self, request, *args, **kwargs):
        return None

def home_view(request, *args, **kwargs):
    return render(request, 'base.html', context=None)


def detail_view(request, *args, **kwargs):
    id = kwargs['id']  # keyword arguments

    post = Post.objects.get(pk=id)

    return HttpResponse(f"<h1>post id in kwargs: {id}</h1>")


def comment(request, *args, **kwargs):
    return HttpResponse("<h1> my post!</h1>")


def getFeed(request):
    user = User.objects.get(pk=cookies['user_id'])
    posts = (post.author == user.id)

    context = {'user': user, 'post_list': posts}

    return http(context)

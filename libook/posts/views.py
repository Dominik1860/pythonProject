from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from .models import Post, Comment, Like
from django.contrib.auth.models import User
from . import forms


class DetailView(TemplateView):
    """
    Detail page of a post
    """
    template_name = 'post/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.get(pk=kwargs['pk'])
        context['comments'] = context['post'].comment_set.all()
        return context

def create_post(request):
    """
    Form to create a new post
    """
    if request.method == "GET":
        form = forms.CreatePostForm({
            'user': request.user.id
        })

        context = {
            'form': form
        }
        return render(request, 'post/create.html', context)

    if request.method == "POST":
        form = forms.CreatePostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('home'))

        return HttpResponse("POST")

# HANDLING COMMENTS AND LIKES

def create_comment(request):
    user = User.objects.get(pk=request.GET.get('user_id'))
    post = Post.objects.get(pk=request.GET.get('post_id'))
    content = request.GET.get('content')

    comment = Comment(user_id=user, post_id=post, content=content)
    comment.save()

    return None

def create_like(request):
    user = User.objects.get(pk=request.GET.get('user_id'))
    post = Post.objects.get(pk=request.GET.get('post_id'))

    like = Comment(user_id=user, post_id=post)
    like.save()

    return None

def remove_comment(request):
    like = Like.objects.get(pk=request.GET.get('id'))
    like.delete()

    return None


def remove_like(request):
    like = Like.objects.get(pk=request.GET.get('id'))
    like.delete()

    return None

# def upload_post(request):
#     """
#     Creates a new post from POST request
#     """
#     user = request.user
#     if request.method == "POST":
#         form = forms.NewPostForm(request.POST, request.FILES)
#         # Validate form and create new post
#         if form.is_valid():
#             data = form.save(commit=False)
#             data.user_name = user
#             data.save()
#             messages.success(request, f'Posted Successfully')
#             return redirect('/home')
#
#         else:
#             form = NewPostForm()
#
#     else:
#     return render(request, 'post/create.html', {'form': form})

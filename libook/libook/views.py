from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.views.generic.list import ListView
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from . import forms
from profiles.models import Profile
from posts.forms import CreatePostForm
from posts.models import Post


# class HomeView(TemplateView):
#     """
#     Shows feed of logged in user. Basically a dashboard.
#     """
#     template_name = 'home/index.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = CreatePostForm({'user': self.request.user.id})
#         context['feed'] = Post.objects.filter(user__id=self.request.user.id)
#         context['logged_user_id'] = self.request.user.id
#         return context

class HomeView(ListView):
    """
    Shows feed of logged in user. Basically a dashboard.
    """
    model = Post
    template_name = 'home/index.html'
    context_object_name = 'feed'

    def get_queryset(self):
        current_user = Profile.objects.get(pk=self.request.user.id)
        # queryset is not iterable, so got to fetch dict using values(), or tuple by values_list()
        friends = current_user.friends.all().values()
        all_posts = Post.objects.filter(user__id=self.request.user.id).order_by('-timestamp')

        for friend in friends:
            # UNION OPERATOR https://stackoverflow.com/questions/29587382/how-to-add-an-model-instance-to-a-django-queryset
            all_posts |= Post.objects.filter(user__id=friend['user_id']).order_by('-timestamp')

        return all_posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CreatePostForm({'user': self.request.user.id})
        # context['feed'] = Post.objects.filter(user__id=self.request.user.id)
        context['logged_user_id'] = self.request.user.id
        return context


def register(request):
    """
    Creates a new user from POST request
    """
    if request.method == 'POST':
        # Validate form and create new user and profile
        user_form = forms.UserRegistrationForm(data=request.POST)
        if user_form.is_valid():
            User.objects.create_user(
                username=request.POST['email'],
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                password=request.POST['password'],
            )

            # https://docs.djangoproject.com/en/3.1/topics/auth/default/#auth-web-requests
            user = authenticate(request,
                                username=request.POST['email'],
                                password=request.POST['password'])

            if user is not None:
                login(request, user)
                return redirect('/home')
        else:
            print(user_form.errors)
    else:
        return redirect('/login')

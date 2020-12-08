from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView, ListView
from django.contrib.auth.models import User
from django.http import HttpResponse
from . import forms
from posts.forms import CreatePostForm
from posts.models import Post


class HomeView(TemplateView):
    """
    Shows feed of logged in user. Basically a dashboard.
    """
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CreatePostForm({'user': self.request.user.id})
        context['feed'] = Post.objects.filter(user__id=self.request.user.id)
        context['logged_user_id'] = self.request.user.id
        return context

    def post(self, request):
        return HttpResponse('POST')


def register(request):
    """
    Creates a new user from POST request
    """
    if request.method == 'POST':
        user_form = forms.UserRegistrationForm(data=request.POST)
        # Validate form and create new user and profile
        if user_form.is_valid():
            User.objects.create_user(
                username=request.POST['email'],
                # email correct?
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                password=request.POST['password'],
            )
            return redirect('/home')
        else:
            print(user_form.errors)
    else:
        return redirect('/login')

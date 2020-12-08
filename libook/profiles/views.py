from django.shortcuts import render, redirect
from django.db.models import Count
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from pathlib import Path
from . import forms
from .models import Profile
from posts.models import Post
import os

BASE_DIR = Path(__file__).resolve().parent.parent


class EditProfileView(FormView):
    """
    Render a form for editing Profile
    """
    template_name = 'profile/edit.html'
    form_class = forms.UpdateProfileForm
    success_url = '/home'
    context = {}

    def get(self, request):
        """
        Handles GET request and returns form for editing
        """
        profile = Profile.objects.get(user=User.objects.get(pk=request.user.id))
        self.context.update(form=forms.UpdateProfileForm(instance=profile))
        self.context.update(mugshot=profile.mugshot)
        self.context.update(user=request.user)
        return render(request, 'profile/edit.html', self.context)

    def post(self, request):
        """
        Handles new changes in POST request
        """
        profile = Profile.objects.get(pk=request.user.id)
        form = forms.UpdateProfileForm(instance=profile, data=request.POST, files=request.FILES)
        if form.is_valid():
            # image = Image.open(form.cleaned_data['mugshot'])
            # image_path = os.path.join((BASE_DIR), 'static/imgs/profile/') + request.user.username + '_mugshot.jpg'
            # image.save(image_path)
            form.save()

        return redirect(to='/profile/edit')


class DetailView(TemplateView):
    """
    Detail page of a profile
    """
    template_name = 'profile/detail.html'

    def get_context_data(self, **kwargs):
        profile = Profile.objects.select_related('user').get(pk=kwargs['pk'])
        context = super().get_context_data(**kwargs)
        context['profile'] = profile
        context['posts'] = Post.objects.filter(user__id=profile.user.id)
        context['number_of_posts'] = context['posts'].count()
        context['friends'] = profile.friends.all()
        context['number_of_friends'] = context['friends'].count()

        return context

# class TestView(View):
#     def get(self, request):
#         return render(request, 'profile/test.html', None)
#
#     def post(self, request):
#         if request.method == 'POST':
#             form = forms.TestForm(request.POST, request.FILES)
#             print(request.POST)
#             print(request.FILES)
#             print('form is post')
#             if form.is_valid():
#                 print('form is valid')
#
#         return redirect('/profile/test/')

from django.shortcuts import render, redirect, reverse
from django.db.models import Count
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from pathlib import Path
from . import forms
from .models import Profile
from posts.models import Post


class EditProfileView(FormView):
    """
    Render a form for editing profile.
    """
    form_class = forms.UpdateProfileForm
    success_url = '/home'
    context = {}

    def get(self, request):
        """
        Handles GET request and returns form for editing.
        """
        profile = Profile.objects.get(user=User.objects.get(pk=request.user.id))
        self.context.update(form=forms.UpdateProfileForm(instance=profile))
        self.context.update(mugshot=profile.mugshot)
        self.context.update(user=request.user)
        return render(request, 'profile/edit.html', self.context)

    def post(self, request):
        """
        Handles new changes in POST request.
        """
        profile = Profile.objects.get(pk=request.user.id)
        form = forms.UpdateProfileForm(instance=profile, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()

        return redirect(reverse('update_profile'))


class DetailView(TemplateView):
    """
    Detail page of a profile.
    """
    template_name = 'profile/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if len(kwargs) == 0:
            profile = Profile.objects.select_related('user').get(pk=self.request.user.id)
        else:
            profile = Profile.objects.select_related('user').get(pk=kwargs['pk'])

        friends = profile.friends.all().values_list()

        if self.request.user.id == profile.user.id:
            context['friendly'] = -1
        elif friends and self.request.user.id in friends[0]:
            context['friendly'] = 1
        else:
            context['friendly'] = 0

        # print(f"request user id = {self.request.user.id}")
        # print(f"profile user id = {profile.user.id}")
        # print(f"friendly = {context['friendly']}")

        context['profile'] = profile
        context['posts'] = Post.objects.filter(user__id=profile.user.id)
        context['friends'] = profile.friends.all()

        return context


def add_friend(request):
    """
    Form to add a friend to a user.
    """
    profile = Profile.objects.get(user__id=request.user.id)
    profile.friends.add(request.GET.get('friend_id'))
    profile.save()

    return None


def remove_friend(request):
    """
    Form to remove a friend from a user.
    """
    profile = Profile.objects.get(user__id=request.user.id)
    profile.friends.remove(request.GET.get('friend_id'))
    profile.save()

    return None

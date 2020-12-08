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
        return render(request, reverse('update_profile'), self.context)

    def post(self, request):
        """
        Handles new changes in POST request
        """
        profile = Profile.objects.get(pk=request.user.id)
        form = forms.UpdateProfileForm(instance=profile, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()

        return redirect(reverse('update_profile'))


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

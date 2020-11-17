from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from . import forms
from .models import Profile

def update_profile(request):
    if request.method == 'POST':
        profile = Profile.objects.get(user=User.objects.get(pk=request.user.id))
        profile.birthdate = request.POST.get('birthdate')
        profile.telephone = request.POST.get('telephone')
        profile.privacy_settings = request.POST.get('privacy_settings')
        profile.save()

    return redirect(to='/profiles/edit')

class EditProfileView(FormView):
    template_name = 'profile/edit.html'
    form_class = forms.UpdateProfileForm
    success_url = '/home'
    context = {}

    def get(self, request):
        """
        Finds Profile using User one-to-one relation, that is found by user.id stored in request
        """
        profile = Profile.objects.get(user=User.objects.get(pk=request.user.id))
        self.context.update(form = forms.UpdateProfileForm(instance=profile))
        return render(request, 'profile/edit.html', self.context)

    # def form_valid(self, form):
    #     form.user = self.request.user
    #     form.instance.save()
    #     return super().form_valid(form)

def detail(request, **kwargs):
    profile_id = kwargs['id']
    # post = Profile.objects.get(pk=profile_id)

    context = {
        'id' : profile_id,
    }

    return render(request, 'profile/detail.html', context)


def profile_list(request, **kwargs):
    each_post = profile_get_next_or_previous_by_FIELD(id = id)
    context ={
        'profile_list': each_post,
        }
    return render(request, 'profile/profile_list.html', context)


def Add_post(request, id):
    each_post = post.objects.get(id = id)
    each_post.Add()
    return render(request, 'each_post/Add.html', context)

def delete_post(request, id):
    each_post = post.objects.get(id = id)
    each_post.delete()
    return HttpResponseRedirect('/post')

def post(request,**kwargs):
    tagger_user = kwargs['id']
    # post = tagger.objects.get(pk=profile_id)

    context = {
        'id' : profile_id,
    }

    return render(request, 'tagger/post.html', context)




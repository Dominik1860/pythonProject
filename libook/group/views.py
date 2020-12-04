from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from .models import Group
from . import forms


class GroupDetailView(TemplateView):
    """
    Detail page of a group
    """
    template_name = 'group/detail.html'

    # def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    context['group'] = Group.objects.get(pk=kwargs['pk'])

    #    return context

    def get_context_data(self, **kwargs):
        profile = Group.objects.select_related('group').get(pk=kwargs['pk'])
        context = super().get_context_data(**kwargs)
        context['group'] = group
        context['posts'] = Post.objects.filter(group__id=group.group.id)
        context['members'] = group.members.all()

        return context

def create_new(request):
    """
    Form to create a new group
    """
    if request.method == "GET":
        form = forms.CreatePostForm({
            'user': request.user.id
        })

        context = {
            'form': form
        }
        return render(request, 'group/create.html', context)

    if request.method == "NEW GROUP":
        form = forms.CreateGroupForm(data=request.GROUP, files=request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('home'))

        return HttpResponse("NEW GROUP")

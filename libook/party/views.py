from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from .models import Party
from . import forms


class PartyDetailView(TemplateView):
    """
    Detail page of a party
    """
    template_name = 'party/detail.html'

    # def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    context['party'] = Party.objects.get(pk=kwargs['pk'])

    #    return context

    def get_context_data(self, **kwargs):
        profile = Group.objects.select_related('party').get(pk=kwargs['pk'])
        context = super().get_context_data(**kwargs)
        context['party'] = party
        context['posts'] = Post.objects.filter(party__id=.party.id)
        context['members'] = party.members.all()

        return context

def create_new(request):
    """
    Form to create a new party
    """
    if request.method == "GET":
        form = forms.CreatePartyForm({
            'party': request.party.id
        })

        context = {
            'form': form
        }
        return render(request, 'party/create.html', context)

    if request.method == "NEW PARTY":
        form = forms.CreatePartyForm(data=request.PARTY, files=request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('home'))

        return HttpResponse("NEW PARTY")

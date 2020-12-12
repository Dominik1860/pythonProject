from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from .models import Party
from . import forms


class PartyListView(ListView):
    """
    Class that returns list of all parties.
    """
    model = Party
    template_name = 'party/index.html'
    ordering = ['timestamp']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class PartyDetailView(TemplateView):
    """
    Class that returns detail page of a party.
    """
    template_name = 'party/detail.html'

    # def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    context['party'] = Party.objects.get(pk=kwargs['pk'])

    #    return context

    def get_context_data(self, **kwargs):
        party = Party.objects.select_related('party').get(pk=kwargs['pk'])
        context = super().get_context_data(**kwargs)
        context['party'] = party
        context['posts'] = Post.objects.filter(party__id=party.id)
        context['members'] = party.members.all()

        return context

def create_new(request):
    """
    Form to create a new party.
    """
    if request.method == "GET":
        form = forms.CreatePartyForm({
            'party': request.party.id
        })

        context = {
            'form': form
        }
        return render(request, 'party/update.html', context)

    if request.method == "NEW PARTY":
        form = forms.CreatePartyForm(data=request.PARTY, files=request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('home'))

        return HttpResponse("NEW PARTY")

def signup(request):
    """
    Form to signup for a party.
    """
    party_id = request.GET.get('party_id')
    user_id = request.user.id

    party = Party.objects.get(pk=party_id)
    event.members.add(user_id)

    return None


def unsubscribe(request):
    """
    Form to unsubscribe from a party.
    """
    party_id = request.GET.get('party_id')
    user_id = request.user.id

    party = party.objects.get(pk=party_id)
    party.members.remove(user_id)

    return None
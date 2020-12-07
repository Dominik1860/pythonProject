from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from .models import Event
from . import forms


class EventDetailView(TemplateView):
    """
    Detail page of an event
    """
    template_name = 'event/detail.html'

    # def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    context['event'] = Event.objects.get(pk=kwargs['pk'])

    #    return context

    def get_context_data(self, **kwargs):
        event = Event.objects.select_related('event').get(pk=kwargs['pk'])
        context = super().get_context_data(**kwargs)
        context['event'] = event
        context['posts'] = Post.objects.filter(event__id=event.id)
        context['members'] = event.members.all()

        return context

def create_new(request):
    """
    Form to create a new event
    """
    if request.method == "GET":
        form = forms.CreateEventForm({
            'event': request.event.id
        })

        context = {
            'form': form
        }
        return render(request, 'event/create.html', context)

    if request.method == "NEW EVENT":
        form = forms.CreateEventForm(data=request.PARTY, files=request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('home'))

        return HttpResponse("NEW EVENT")

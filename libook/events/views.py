from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from .models import Event
from profiles.models import Profile
from . import forms


class EventListView(ListView):
    """
    returns list of all events
    """
    model = Event
    template_name = 'event/index.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class EventUserFilteredListView(ListView):
    """
    returns list of all events
    """
    model = Event
    template_name = 'event/my_events.html'
    paginate_by = 10
    ordering = ['-timestamp']

    def get_queryset(self):
        """Overrides conventional queryset attribute, so you can access request property and get user ID"""
        return Event.objects.filter(members__id=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class EventDetailView(TemplateView):
    """
    Detail page of an event
    """
    template_name = 'event/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event'] = Event.objects.get(pk=kwargs['pk'])
        context['members'] = context['event'].members.all()
        context['admin'] = Profile.objects.get(user=context['event'].admin)
        context['issignedup'] = Event.objects.filter(
            members__id=self.request.user.id).count()  # Checks if current user is singed in

        print(context['issignedup'])

        return context


def signup(request):
    event_id = request.GET.get('event_id')
    user_id = request.user.id

    event = Event.objects.get(pk=event_id)
    event.members.add(user_id)

    return None


def unsubscribe(request):
    event_id = request.GET.get('event_id')
    user_id = request.user.id

    event = Event.objects.get(pk=event_id)
    event.members.remove(user_id)

    return None


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

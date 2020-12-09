from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, FormView
from .models import Event
from profiles.models import Profile
from . import forms
from datetime import datetime


class EventListView(ListView):
    """
    returns list of all events
    """
    model = Event
    template_name = 'event/index.html'
    ordering = ['timestamp']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class EventUserFilteredListView(ListView):
    """
    returns list of all events
    """
    model = Event
    template_name = 'event/my_events.html'
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
        if context['event'].admin.id == self.request.user.id:
            context['isowner'] = 1

        return context


class EventCreateView(FormView):
    form_class = forms.CreateEventForm()
    context = {}

    def get(self, request, **kwargs):
        event = Event.objects.create(
            admin=self.request.user
        )
        form = forms.CreateEventForm(instance=event)
        self.context.update(form=form)

        return render(request, 'event/update.html', self.context)

    def post(self, request):
        form = forms.CreateEventForm(data=request.POST)

        if form.is_valid():
            form.save(commit=True)

        return HttpResponseRedirect(reverse('list_event'))


class EventUpdateView(FormView):
    form_class = forms.CreateEventForm()
    context = {}

    def get(self, request, **kwargs):
        event = Event.objects.get(pk=kwargs['pk'])
        form = forms.CreateEventForm(instance=event)
        self.context.update(form=form)

        return render(request, 'event/update.html', self.context)


def create(request):
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
        return render(request, 'event/update.html', context)

    if request.method == "NEW EVENT":
        form = forms.CreateEventForm(data=request.PARTY, files=request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('home'))

        return HttpResponse("NEW EVENT")


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

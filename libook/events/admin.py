from django.contrib import admin
from .models import Event, EventInvitationRequest

admin.site.register(Event)
admin.site.register(EventInvitationRequest)
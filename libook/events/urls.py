from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create_new, name='create_event'),
    path('detail/<int:pk>', views.EventDetailView.as_view(), name='detail_event')
]
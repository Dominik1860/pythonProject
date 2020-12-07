from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('/new', views.create_new, name='create_new'),
    path('/detail/<int:pk>', views.EventDetailView.as_view(), name='event_detail')
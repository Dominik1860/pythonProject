from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create_new, name='create_party'),
    path('detail/<int:pk>', views.PartyDetailView.as_view(), name='detail_party')
]
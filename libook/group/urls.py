from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('/new', views.CreateNewGroupView.as_view(), name='group_new'),
    path('/detail/<int:pk>', views.GroupDetailView.as_view(), name='group_detail')
]
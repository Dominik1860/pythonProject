from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.EventListView.as_view(), name='list_event'),
    path('myevents/', views.EventUserFilteredListView.as_view(), name='list_user_events'),
    path('create/', views.create_new, name='create_event'),
    path('detail/<int:pk>', views.EventDetailView.as_view(), name='detail_event'),
    path('signup/', views.signup,),
    path('unsubscribe/', views.unsubscribe,),
]
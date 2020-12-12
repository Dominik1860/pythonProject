from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.EventListView.as_view(), name='list_event'),
    path('myevents/', views.EventUserFilteredListView.as_view(), name='my_events'),
    path('create/', views.EventCreateView.as_view(), name='create_event'),
    path('update/<int:pk>', views.EventUpdateView.as_view(), name='update_event'),
    path('detail/<int:pk>', views.EventDetailView.as_view(), name='detail_event'),
    path('signup/', views.signup, ),
    path('unsubscribe/', views.unsubscribe, ),
]

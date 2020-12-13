from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.PartyListView.as_view(), name='list_party'),
    path('myevents/', views.PartyUserFilteredListView.as_view(), name='my_party'),
    path('create/', views.PartyCreateView.as_view(), name='create_party'),
    path('update/<int:pk>', views.PartyUpdateView.as_view(), name='update_party'),
    path('detail/<int:pk>', views.PartyDetailView.as_view(), name='detail_party'),
    path('signup/', views.signup, ),
    path('unsubscribe/', views.unsubscribe, ),
]
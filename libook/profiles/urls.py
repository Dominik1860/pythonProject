from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.ProfileListView.as_view(), name='list_profile'),
    path('update/', views.EditProfileView.as_view(), name='update_profile'),
    path('detail/', views.DetailView.as_view(), name='my_profile'),
    path('detail/<int:pk>', views.DetailView.as_view(), name='detail_profile'),
    path('addfriend/', views.add_friend, ),
    path('removefriend/', views.remove_friend),
]

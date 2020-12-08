from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('update/', views.EditProfileView.as_view(), name='update_profile'),
    path('detail/<int:pk>', views.DetailView.as_view(), name='detail_profile'),
    # path('test/', views.TestView.as_view(), name='test_post'),
]

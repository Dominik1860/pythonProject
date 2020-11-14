from django.urls import path
from . import views

urlpatterns = [
    path('edit/', views.EditProfileView.as_view(), name='edit_profile'),
    path('edit/update-profile', views.update_profile, name='update_profile'),
]

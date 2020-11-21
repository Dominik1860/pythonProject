from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:pk>', views.DetailView.as_view(), name='post_detail'),
    path('create-post/', views.create_post, name='create_post')
]


from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:id>', views.detail, name='post_detail'),
    path('create-post/', views.create_post, name='create_post')
]


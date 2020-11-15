from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:id>', views.detail, name='post_detail'),
    path('upload-post/', views.upload_post, name='post_upload_post')
]

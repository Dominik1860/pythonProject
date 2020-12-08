from django.urls import path, include
from . import views

# https://docs.djangoproject.com/en/3.1/topics/http/urls/#including-other-urlconfs

comment_urlpattern = [
    path('create/', views.create_comment, name='create_comment'),
    path('remove/', views.remove_comment, name='remove_comment'),
]

like_urlpattern = [
    path('create/', views.create_like, name='create_like'),
    path('remove/', views.remove_like, name='remove_like'),
]

urlpatterns = [
    path('create/', views.create_post, name='create_post'),
    path('detail/<int:pk>/', views.DetailView.as_view(), name='detail_post'),
    path('like/', include(like_urlpattern)),
    path('comment/', include(comment_urlpattern)),
]

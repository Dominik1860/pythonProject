from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view),
    path('<int:id>/', views.detail_view),
]

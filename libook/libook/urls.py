from django.contrib import admin
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import include, path
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    # path('', views.LoginView.as_view()),
    path('', RedirectView.as_view(url='/login')),
    path('', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('home/', login_required(views.HomeView.as_view())),
    path('posts/', include('posts.urls')),
    path('users/', include('users.urls')),
]

# path('accounts/', include('django.contrib.auth.urls')),
# accounts/ login/ [name='login']
# accounts/ logout/ [name='logout']
# accounts/ password_change/ [name='password_change']
# accounts/ password_change/done/ [name='password_change_done']
# accounts/ password_reset/ [name='password_reset']
# accounts/ password_reset/done/ [name='password_reset_done']
# accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/ reset/done/ [name='password_reset_complete']



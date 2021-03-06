from django.contrib import admin
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import include, path
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # Authentication
    path('', RedirectView.as_view(url='/login')),  # Default redirect to /login
    path('', include('django.contrib.auth.urls')),  # All login requests
    path('home/', login_required(views.HomeView.as_view()), name='home'),  # Dashboard for logged in user
    path('register/', views.register, name='register'),  # Register a new user

    # Individual apps
    path('posts/', include('posts.urls')),
    path('profile/', include('profiles.urls')),
    path('events/', include('events.urls')),
    path('party/', include('party.urls')),
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

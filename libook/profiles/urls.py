from django.contrib import admin
from django.urls import path
from . import views import profile_list, each_post, delete_friend, tagger_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('edit/', views.EditProfileView.as_view(), name='edit_profile'),
    path('edit/update-profile', views.update_profile, name='update_profile'),
    path('detail/<int:id>', views.detail, name='profile_detail'),
]

urlpatterns =[
    path('',profile_list),
    path('<id>/',each_post),
]

urlpatterns =[
    path('',profile_list),
    path('<id>/',each_post),
    path('<id>/delete/'Add_post)
]

urlpatterns =[
    path('',profile_list),
    path('<id>/',each_post),
    path('<id>/delete/'delete_post)
]

urlpatterns =[
    path('',tagger_user),
    path('<id>/',each_post),
]
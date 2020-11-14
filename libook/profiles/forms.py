from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from profiles.models import Profile


# from .models import Profile

class UserRegisterForm(UserCreationForm):
    """
    Registers a new user on /login page
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UpdateProfileForm(forms.ModelForm):
    """
    Updates a logged in user on /profile/edit
    """

    user = forms.IntegerField(
        disabled=True
    )
    birthdate = forms.DateField(
        # widget=forms.DateInput(format='%d.%m.%Y'),
        # input_formats=['%d.%m.%Y'],
    )

    class Meta:
        model = Profile
        fields = '__all__'



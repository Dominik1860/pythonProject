from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from profiles.models import Profile


class UserRegisterForm(UserCreationForm):
    """
    Registers a new user on /login page
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class UpdateProfileForm(forms.ModelForm):
    """
    Updates a logged in user on /profile/edit
    """

    def __init__(self, *args, **kwargs):
        super(UpdateProfileForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    user = forms.IntegerField(
        widget=forms.HiddenInput()
    )

    class Meta:
        model = Profile
        exclude = ('friends',)

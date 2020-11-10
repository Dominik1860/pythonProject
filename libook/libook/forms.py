from django import forms
from django.contrib.auth.models import User

class CommentForm(forms.Form):
    content = forms.CharField(label='Content', max_length=255)
    image = forms.ImageField(allow_empty_file=True)

class UserRegistrationForm(forms.ModelForm):
    """
    Form to register a new user.
    """

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

    # first_name = forms.CharField()
    # last_name = forms.CharField()
    # email = forms.CharField()
    # password = forms.CharField()

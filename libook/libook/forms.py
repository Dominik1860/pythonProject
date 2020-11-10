from django import forms
from users.models import User

class CommentForm(forms.Form):
    content = forms.CharField(label='Content', max_length=255)
    image = forms.ImageField(allow_empty_file=True)

class RegistrationForm(forms.ModelForm):
    """
    Form to register a new user.
    """
    class Meta:
        model = User
        fields = '__all__'
        exclude = ('privacy_settings',)


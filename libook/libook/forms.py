from django import forms

class CommentForm(forms.Form):
    content = forms.CharField(label='Content', max_length=255)
    image = forms.ImageField(allow_empty_file=True)

class UserForm(forms.Form):
    """
    Form to register a new user.
    """

    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()
    password = forms.CharField()

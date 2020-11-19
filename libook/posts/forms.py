from django import forms
from .models import Post


class CreatePostForm(forms.ModelForm):
    """
    Form for creating a new post entity
    """

    def __init__(self, *args, **kwargs):
        """
        https://stackoverflow.com/questions/31627253/django-modelform-with-bootstrap
        """
        super(CreatePostForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

        self.fields['user'].widget.attrs['class'] = 'form-control user-hidden-field'


    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['number_of_likes']

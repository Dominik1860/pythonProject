from django import forms
from .models import Group

class CreateGroupForm(forms.ModelForm):
    """
    Form for creating a new group entity
    """

    def __init__(self, *args, **kwargs):
        """
        https://stackoverflow.com/questions/31627253/django-modelform-with-bootstrap
        """
        super(CreateGroupForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

        self.fields['user'].widget.attrs['class'] = 'form-control user-hidden-field'


    class Meta:
        model = Group
        fields = '__all__'



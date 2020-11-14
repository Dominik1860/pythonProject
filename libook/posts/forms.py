from django import forms
from .models import Post

class CreatePostForm(forms.ModelForm):

    name = forms.CharField(
        widget=forms.HiddenInput(),
        initial='random_hash' # random UID for textual posts
    )

    post_type = forms.IntegerField(
        widget=forms.HiddenInput(),
        initial=1 # TEXT
    )

    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['number_of_likes', 'tagged_user_id', 'name']
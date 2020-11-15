from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .models import Post
from . import forms


def detail(request, **kwargs):
    post_id = kwargs['id']
    # post = Post.objects.get(pk=post_id)

    context = {
        'id' : post_id,
        'test': 'test',
        'test_number': 1
    }

    return render(request, 'post/detail.html', context)


def upload_post(request):
    """
    Creates a new post from POST request
    """
	user = request.user
	if request.method == "POST":
		form = NewPostForm(request.POST, request.FILES)
        # Validate form and create new post
		if form.is_valid():
			data = form.save(commit=False)
			data.user_name = user
			data.save()
			messages.success(request, f'Posted Successfully')
			return redirect('/home')
	else:
		form = NewPostForm()

	    else:
            return render(request, 'post/upload_post.html', {'form':form})
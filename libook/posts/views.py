from django.shortcuts import render, reverse, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .models import Post, Comment, Like
from django.contrib.auth.models import User
from . import forms


class UpdatePostView(FormView):
    """
    Render a form for editing Profile
    """
    form_class = forms.CreatePostForm()
    context = {}

    def get(self, request, **kwargs):
        """
        Handles GET request and returns form for editing
        """
        post = Post.objects.get(pk=kwargs['pk'])
        self.context.update(post_id=post.id)
        self.context.update(post_image=post.image)
        self.context.update(form=forms.CreatePostForm(instance=post))
        return render(request, 'post/update.html', self.context)

    def post(self, request, pk):
        """
        Handles new changes in POST request
        """
        post = Post.objects.get(pk=pk)
        form = forms.CreatePostForm(instance=post, data=request.POST, files=request.FILES)

        if form.is_valid():
            form.save()
        return redirect(f'/posts/detail/{post.id}')


class DetailView(TemplateView):
    """
    Detail page of a post
    """
    template_name = 'post/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.get(pk=kwargs['pk'])
        context['comments'] = context['post'].comment_set.all().order_by('-timestamp')
        context['likes'] = context['post'].like_set.all()
        return context


def create_post(request):
    """
    Form to create a new post
    """
    if request.method == "GET":
        # try:
        form = forms.CreatePostForm({
            'user': request.user.id
        })

        context = {
            'form': form
        }
        return render(request, 'post/update.html', context)

    # except SomeRandomError:
    #     return Http302 ("Bad request, something went wrong")

    # else:
    #    return Http302 ("Form is invalid")

    if request.method == "POST":
        form = forms.CreatePostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('home'))

        return HttpResponse("POST")


# HANDLING COMMENTS AND LIKES

def create_comment(request):
    user = request.user
    post = Post.objects.get(pk=request.GET.get('post_id'))
    content = request.GET.get('content')

    comment = Comment(user_id=user, post_id=post, content=content)
    comment.save()

    return None


def create_like(request):
    user = request.user
    post = Post.objects.get(pk=request.GET.get('post_id'))

    like = Like(user_id=user, post_id=post)
    like.save()

    return None

# def upload_post(request):
#     """
#     Creates a new post from POST request
#     """
#     user = request.user
#     if request.method == "POST":
#         form = forms.NewPostForm(request.POST, request.FILES)
#         # Validate form and create new post
#         if form.is_valid():
#             data = form.save(commit=False)
#             data.user_name = user
#             data.save()
#             messages.success(request, f'Posted Successfully')
#             return redirect('/home')
#
#         else:
#             form = NewPostForm()
#
#     else:
#     return render(request, 'post/update.html', {'form': form})

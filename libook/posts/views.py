from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from .models import Post
from . import forms


class DetailView(TemplateView):
    """
    Detail page of a post
    """
    template_name = 'post/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.get(pk=kwargs['pk'])

        return context


def create_post(request):
    """
    Form to create a new post
    """
    if request.method == "GET":
        form = forms.CreatePostForm({
            'user': request.user.id
        })

        context = {
            'form': form
        }
        return render(request, 'post/create.html', context)

    if request.method == "POST":
        form = forms.CreatePostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('home'))

        return HttpResponse("POST")

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
#     return render(request, 'post/create.html', {'form': form})

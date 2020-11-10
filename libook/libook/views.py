from django.shortcuts import render
from . import forms

def index(request):
    # not logged in, register form
    form = forms.RegistrationForm()
    return render(request, 'home/index.html', context= { 'registration_form': form })

    # logged in
    form = forms.CommentForm()
    return render(request, 'home/index.html', context={ 'form': form })

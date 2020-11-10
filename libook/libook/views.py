from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from . import forms


class LoginView(View):
    context = {'form': forms.UserForm()}

    def get(self, request):
        return render(request, 'home/login.html', self.context)

class HomeView(View):
    context = {}

    def get(self, request):
        return render(request,'home/index.html', self.context)

def index(request):
    # not logged in, register form
    form = forms.RegistrationForm()
    return render(request, 'home/login.html', context={'registration_form': form})

    # logged in
    form = forms.CommentForm()
    return render(request, 'home/index.html', context={'form': form})

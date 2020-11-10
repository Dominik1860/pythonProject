from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from . import forms


class HomeView(View):
    context = {}

    def get(self, request):
        return render(request, 'home/index.html', self.context)


def register(request):
    """
    Creates a new user from POST request
    """
    if request.method == 'POST':
        user_form = forms.UserRegistrationForm(data=request.POST)
        # Validate form and create new user and profile
        if user_form.is_valid():
            User.objects.create_user(
                username=request.POST['email'],
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                password=request.POST['password'],
            )
            return redirect('/home')
        else:
            print(user_form.errors)
    else:
        return redirect('/login')


from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from . import forms
from .models import Profile


class EditProfileView(View):
    context = {

    }

    def get(self, request):
        print(request.user.id)
        self.context.update(form = forms.UserUpdateForm(instance=request.user))
        return render(request, 'profile/edit.html', self.context)

    def post(self, request):
        return HttpResponse("<h1>VALID SUBMISSION</h1>")
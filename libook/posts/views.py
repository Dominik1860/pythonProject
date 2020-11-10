from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.

def home_views(*args, **kwargs):
    return HttpResponse("<h1>welcome to my web !</h1>""")

class IndexView(View):
    def post(self, request, *args, **kwargs):
        return HttpResponse("views")


def comment(self,request,*args, **kwargs):
   return HttpResponse("<h1> my post!</h1>")



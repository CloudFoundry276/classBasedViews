from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse


# Create your views here.
class GreetingView(View):
    greeting_message = "<b>First Class Based View!</b>"

    def get(self, request):
        return HttpResponse(self.greeting_message)

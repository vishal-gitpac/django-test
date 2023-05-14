from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response
# request handler


def say_hello(request):
    # pull data
    # transform data
    # send email
    return render(request, "hello.html", {"name": "Vishal"})

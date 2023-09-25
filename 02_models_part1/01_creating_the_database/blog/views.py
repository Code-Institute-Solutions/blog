from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def myblog(request):
    return HttpResponse("Hello, Blog!")

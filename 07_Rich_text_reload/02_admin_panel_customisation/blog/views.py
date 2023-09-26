from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1)
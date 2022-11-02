from django.shortcuts import render
from requests import post
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def blog(request):
    # posts = Post.objects.get(id=pk)
    return render(request, 'blog.html')

def post(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'posts.html', {'post': post})


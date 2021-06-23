from django import http
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
# Create your views here.
def index(request):
    allPosts= Post.objects.all()
    context={'allPosts': allPosts}
    return render(request,'blog/blog.html', context)

def blogPost(request, slug): 
    post=Post.objects.filter(slug=slug).first()
    context={"post":post}
    return render(request, "blog/blogPost.html", context)


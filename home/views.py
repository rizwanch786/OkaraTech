from django.shortcuts import render
from django.http import HttpResponse
from home.models import Contact
from blog.models import Post
# Create your views here.
def home(request):
    return render(request,'home/home.html')



import os
from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.ERROR:'danger'
}

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.ERROR(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, "home/contact.html")


def about(request):
    return render(request,'home/about.html')



def search(request):
    query=request.GET['search']
    if len(query)>78:
        allPosts=Post.objects.none()
    else:
        allPostsTitle= Post.objects.filter(title__icontains=query)
        allPostsAuthor= Post.objects.filter(author__icontains=query)
        allPostsContent =Post.objects.filter(content__icontains=query)
        allPosts=  allPostsTitle.union(allPostsContent, allPostsAuthor)
    params={'allPosts': allPosts, 'query': query}
    return render(request, 'home/search.html', params)
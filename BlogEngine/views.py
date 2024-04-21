from django.shortcuts import render
from .models import BlogPost

def index(request):
    print("Rendering index.html")
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def topics_detail(request):
    return render(request, 'topics-detail.html')

def topics_listing(request):
    return render(request, 'topics-listing.html')

def blog_list(request):
    posts = BlogPost.objects.filter(live=True)
    return render(request, 'blog-list.html', {'posts': posts})
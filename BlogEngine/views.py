from django.shortcuts import render, get_object_or_404
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

def posts_listing(request):
    posts = BlogPost.objects.filter(live=True).order_by('-updated_at')
    return render(request, 'posts-list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, live=True)  # Ensure the post is live
    return render(request, 'post-detail.html', {'post': post})


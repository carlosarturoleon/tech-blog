from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def index(request):
    print("Rendering index.html")
    return render(request, 'index.html')

def contact(request):
    post = 'Contact Form'
    breadcrumbs = [
        ('index', 'Homepage'),
        ('contact', 'Contact Form')
    ]

    context = {
        'post': post,
        'breadcrumbs': breadcrumbs
    }
    return render(request, 'contact.html', context)

def topics_detail(request):
    return render(request, 'topics-detail.html')

def topics_listing(request):
    post = 'Topic Listing'
    breadcrumbs = [
        ('index', 'Homepage'),
        ('topics_listing', 'Topic Listing')
    ]

    context = {
        'post': post,
        'breadcrumbs': breadcrumbs
    }
    return render(request, 'topics-listing.html', context)

def posts_listing(request):
    posts = BlogPost.objects.filter(live=True).order_by('-updated_at')
    post = 'Blog Posts'
    breadcrumbs = [
        ('index', 'Homepage'),
        ('contact', 'Contact Form')
    ]

    context = {
        'posts': posts,
        'post': post,
        'breadcrumbs': breadcrumbs
    }
    return render(request, 'posts-list.html', context)

def post_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, live=True)  # Ensure the post is live

    # Dynamic breadcrumbs setup
    breadcrumbs = [
        ('index', 'Homepage'),  # Static homepage breadcrumb
        ('post', 'Posts'),
        ('post_detail', post.title)  # Dynamic breadcrumb based on the post's title
    ]

    context = {
        'post': post,
        'breadcrumbs': breadcrumbs  # Include the breadcrumbs in the context
    }
    return render(request, 'post-detail.html', context)


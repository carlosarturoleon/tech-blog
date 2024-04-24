from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import ContactForm 
from django.contrib import messages

def index(request):
    print("Rendering index.html")
    return render(request, 'index.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Here, you would typically handle the validated data.
            # For example, send an email, save the data to a database, etc.
            # After processing the data, redirect to a new URL:
            messages.success(request, 'Your message has been sent successfully!')

            return redirect('contact')  # Redirect to a 'thank you' page, for instance.
    else:
        form = ContactForm()  # An unbound form for GET requests

    post = 'Contact Form'
    breadcrumbs = [
        ('index', 'Homepage'),
        ('contact', 'Contact Form')
    ]

    context = {
        'form': form,
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


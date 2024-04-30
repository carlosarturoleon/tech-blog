from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost, Contact, Glossary
from .forms import ContactForm 
from django.contrib import messages


def index(request):
    print("Rendering index.html")
    return render(request, 'index.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = Contact(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            )
            contact.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')  
        else:
            print("Form is not valid")
            print(form.errors)
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


def glossary_listing(request):
    glossary = Glossary.objects.order_by('term')
    glossary_by_letter = {}
    for item in glossary:
        first_letter = item.term[0].upper() 
        if first_letter not in glossary_by_letter:
            glossary_by_letter[first_letter] = []
        glossary_by_letter[first_letter].append(item)
        
    glossary_breadcrumbs = 'Glossary'
    breadcrumbs = [
        ('index', 'Homepage'),
        ('glossary_listing', 'Glossary')
    ]

    context = {
        'glossary': glossary_by_letter,
        'post': glossary_breadcrumbs,
        'breadcrumbs': breadcrumbs
    }
    return render(request, 'glossary_list.html', context)


def glossary_detail(request, slug):
    glossary_item = get_object_or_404(Glossary, slug=slug)
    breadcrumbs = [
        ('index', 'Homepage'),  # Static homepage breadcrumb
        ('glossary_listing', 'Glossary'),
        ('glossary_detail', glossary_item.term)  # Dynamic breadcrumb based on the post's title
    ]

    context = {
        'glossary': glossary_item,
        'post': glossary_item.term,
        'breadcrumbs': breadcrumbs 
    }
    return render(request, 'glossary_detail.html', context)

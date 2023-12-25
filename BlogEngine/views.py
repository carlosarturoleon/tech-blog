from django.shortcuts import render

def index(request):
    print("Rendering index.html")
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def topics_detail(request):
    return render(request, 'topics-detail.html')

def topics_listing(request):
    return render(request, 'topics-listing.html')

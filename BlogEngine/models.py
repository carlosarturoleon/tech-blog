from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)  # Added slug field
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    live = models.BooleanField(default=False) # Controls visibility of the blog post
    description = models.TextField(blank=True)  # Optional description field
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)  # Image field
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    tags = models.ManyToManyField('Tag', related_name='posts')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # Auto-generate slug from title
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    @property
    def blog_count(self):
        # This uses the related_name 'posts' specified in the BlogPost model.
        return self.posts.count()


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}"



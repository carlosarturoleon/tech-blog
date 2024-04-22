import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project.settings")
django.setup()

from BlogEngine.models import BlogPost
from django.utils.text import slugify
from django.db.utils import IntegrityError

posts = BlogPost.objects.all()

for post in posts:
    if not post.slug:
        original_slug = slugify(post.title)
        slug = original_slug
        counter = 1
        while True:
            try:
                post.slug = slug
                post.save()
                break
            except IntegrityError:
                slug = f"{original_slug}-{counter}"
                counter += 1
        print(f"Updated post: {post.title} with slug: {post.slug}")

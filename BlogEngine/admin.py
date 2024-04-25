from django.contrib import admin
from .models import BlogPost, Contact, Category

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'live', 'created_at', 'updated_at')  
    list_editable = ('live',)  
    search_fields = ('title', 'content', 'author__username')
    list_filter = ('live', 'created_at', 'categories', 'tags')  
    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'description', 'image')
        }),
        ('Content', {
            'fields': ('content',)
        }),
        ('Categorization', {
            'fields': ('categories', 'tags')
        }),
        ('Visibility', { 
            'fields': ('live',)
        }),
        ('Dates', {
            'fields': ('created_at', 'updated_at')
        }),
    )
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Contact)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'blog_count_display', 'description')

    def blog_count_display(self, obj):
        # This method is used to display the count of blog posts in the admin.
        return obj.posts.count()
    blog_count_display.short_description = 'Number of Posts'

# Register your models here.
admin.site.register(Category, CategoryAdmin)

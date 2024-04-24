from django.contrib import admin
from .models import BlogPost, Contact

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

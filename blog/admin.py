from django.contrib import admin

# Register your models here.
from blog.models import Post, Author, Tag


class PostAdmin(admin.ModelAdmin):
    list_filter = ('author', 'tags', 'published_on')
    list_display = ('title', 'author', 'published_on', 'last_updated')
    prepopulated_fields = {"slug": ('title',)}


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)

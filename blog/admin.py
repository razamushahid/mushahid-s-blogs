from django.contrib import admin

# Register your models here.
from blog.models import Post, Author, Tag, Comment


class PostAdmin(admin.ModelAdmin):
    list_filter = ('author', 'tags', 'published_on')
    list_display = ('title', 'author', 'published_on', 'last_updated')
    prepopulated_fields = {"slug": ('title',)}


class CommentAdmin(admin.ModelAdmin):
    list_filter = ("post",)
    list_display = ("user_name", "post", "text")


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)

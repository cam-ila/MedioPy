from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display =  ( 'title', 'author', 'content' )
    list_filter = ('title',)

admin.site.register(Post, PostAdmin) 

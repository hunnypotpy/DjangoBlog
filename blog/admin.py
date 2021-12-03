from django.contrib import admin
from . import models
from .models import Blog, Comment

admin.site.register(models.Blog)

class CommentAdmin(admin.ModelAdmin):
    #list_display = ('name', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'body')
    actions = ['approve_comments']

#corey
'''from django.contrib import admin
from .models import Post

admin.site.register(Post)'''






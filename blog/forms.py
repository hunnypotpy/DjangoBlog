from django.forms import ModelForm

from .models import Blog, Comment, Image


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'post']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')


class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ('image',)

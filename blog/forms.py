from django.forms import ModelForm

from .models import Blog, Comment, Image

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'post', 'slug', 'cover']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

class ImageForm(ModelForm):
    #Form for the image model
    class Meta:
        model = Image
        fields = ('title', 'image')

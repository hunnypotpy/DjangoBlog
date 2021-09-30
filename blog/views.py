from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from .models import Blog, Comment

from .models import Blog
from .forms import BlogForm, CommentForm, ImageForm


def blog_list(request):
    posts = Blog.objects.all()
    return render(request, 'blog/list.html', {'posts': posts})


def blog_detail(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    form = ImageForm(request.POST or None)
    context = {'post': post, 'form': form}
    return render(request, 'blog/detail.html', context)


@login_required
def blog_new(request):
    blog_form = BlogForm(request.POST or None)
    image_form = ImageForm(request.POST or None, request.FILES)

    if blog_form.is_valid() and image_form.is_valid():
        blog = blog_form.save(commit=False)
        blog.user = request.user
        blog.save()

        # TODO: this needs to be multiple images
        im = image_form.save(commit=False)
        im.blog = blog
        im.save()

        messages.success(request, 'Added post')
        return redirect('blog:blog_list')

    context = {'form': blog_form, 'image_form': image_form}
    return render(request, 'blog/form.html', context)


@login_required
def blog_edit(request, pk):
    # Nth time around / editing, check if owner is accessing
    post = get_object_or_404(Blog, pk=pk, user=request.user)
    form = BlogForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, 'Updated post')
        return redirect('blog:blog_list')

    return render(request, 'blog/form.html', {'post': post,
                                              'form': form})

@login_required
def blog_delete(request, pk):
    # Nth time around / editing, check if owner is accessing
    post = get_object_or_404(Blog, pk=pk, user=request.user)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Deleted post')
        return redirect('blog:blog_list')

    return render(request, 'blog/delete.html', {'post': post})

@login_required
def post_detail(request, slug):
    template_name = 'post_detail.html'
    blog = get_object_or_404(Blog, slug=slug)

    # List of active comments for this post
    new_comment = None

    comment_form = CommentForm(request.POST or None)

    if request.method == 'POST':
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.blog = blog
            new_comment.author = request.user
            new_comment.save()

    comments = blog.comments.filter(active=True)

    return render(request,
                    'blog/post_detail.html',
                    {'blog': blog,
                    'comments': comments,
                    'comment_form': comment_form})

def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form})

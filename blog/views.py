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
    return render(request, 'blog/detail.html', {'post': post})


@login_required
def blog_new(request):
    form = BlogForm(request.POST or None)
    # first time around set the user / owner
    if form.is_valid():
        blog = form.save(commit=False)
        blog.user = request.user
        blog.save()

        messages.success(request, 'Added post')
        return redirect('blog:blog_list')
    return render(request, 'blog/form.html', {'form': form})


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
def post_detail(request, slug, year, month, date, post):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish_year=year,
                             publish_month=month,
                             publish_day=day)

    # List of active comments for this post
    comments = post.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(date=request.POST)
        if comment_form_is_valid():
            #Create Comment object but doesn't save database yet
            new_comment = comment_form.save(comment=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save comment to the database
            new_comment.save()
        else:
            comment_form = CommentForm()
        return render(request,
                      'blog/post_detail.html',
                      {'post': post,
                       'comments': comments,
                       'new_comment': new_comment,
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

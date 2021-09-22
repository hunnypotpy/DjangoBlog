from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from .models import Blog

from .models import Blog
from .forms import BlogForm


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

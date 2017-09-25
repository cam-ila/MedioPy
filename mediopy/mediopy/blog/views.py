"""Blog views."""

from django.shortcuts import (redirect, render)
from blog.models import Post
from blog.forms import PostForm


def new_post(request):
    """Create a new post."""
    if request.method == "GET":
        form = PostForm()
        return render(request, 'blog/newpost.html', {'form': form})

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post-list')
        return render(request, 'blog/newpost.html', {'form': form})


def post_list(request):
    """Return a list of posts."""
    posts = Post.objects.all()  # pylint: disable=E1101
    return render(request, 'blog/postlist.html', {'posts': posts})

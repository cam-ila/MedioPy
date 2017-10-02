"""Blog views."""
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login
from django.views.generic import ListView
from django.views.generic import FormView 
from django.views.generic import CreateView
from django.contrib.auth.models import User
from blog.models import Post

#from blog.forms import PostForm 
#from django.shortcuts import (redirect, render)
#def new_post(request):
#    """Create a new post."""
#    if request.method == "GET":
#        form = PostForm()
#        return render(request, 'blog/newpost.html', {'form': form})
#
#    if request.method == "POST":
#        form = PostForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('post-list')
#        return render(request, 'blog/newpost.html', {'form': form})
#

class PostCreate(CreateView):
    model = Post
    fields = '__all__'
    success_url = '/blog'

#def post_list(request):
#    """Return a list of posts."""
#    posts = Post.objects.all()  # pylint: disable=E1101
#    return render(request, 'blog/postlist.html', {'posts': posts})


class PostListView(ListView):
    """post class-based view"""
    model = Post


class LoginView(FormView):
    #TODO: Hacer que ande el form, si es valido que haga algo, o algo asi. no funca
    success_url = '/blog'
    form_class = AuthenticationForm 
    redirect_field_name = REDIRECT_FIELD_NAME
    template_name = 'registration/login.html'
    
    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form) 
    

"""Blog urls."""

from django.conf.urls import url
from blog.views import (PostCreate, PostListView, LoginView)

urlpatterns = [
    url(r'^new/', PostCreate.as_view(), name='new-post'),
    url(r'^$', PostListView.as_view(), name='post-list'),
    url(r'^login/', LoginView.as_view(), name='login'),
]

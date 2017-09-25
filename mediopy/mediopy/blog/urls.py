"""Blog urls."""

from django.conf.urls import url
from blog.views import (new_post, post_list)

urlpatterns = [
    url(r'^new/', new_post, name='new-post'),
    url(r'^$', post_list, name='post-list'),
]

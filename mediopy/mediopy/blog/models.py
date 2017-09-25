"""Blog models."""

from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class Post(models.Model):
    """Author model."""
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return slugify(self.title)



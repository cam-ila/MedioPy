"""Blog forms."""

from django import forms
from blog.models import Post


class PostForm(forms.ModelForm):
    """Post form."""

    class Meta:  # pylint: disable=C0111,R0903
        model = Post
        fields = '__all__'
        widgets = {
            'author': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control editable'}),

        }

from django import forms

from .forms import PostForm

class PostForm(forms.ModelsForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'username', 'date')
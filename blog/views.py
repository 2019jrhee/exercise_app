from django.shortcuts import render
from .models import Post
from .forms import PostForm



def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)

def about (request):
	return render(request, 'blog/about.html', {'title': 'About'})

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
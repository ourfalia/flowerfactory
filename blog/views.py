from django.shortcuts import render
from .models import Post

# Create your views here.

def post_list(request):
    post_list = Post.objects.all()

    context = {
        'post_list': post_list,
    }

    return render(request, 'blog/post_list.html', context)

def post_details(request, id):
    post_details = Post.objects.get(id=id)

    context = {
        'post_details': post_details,
    }

    return render(request, 'blog/post_details.html', context)


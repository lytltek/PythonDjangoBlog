from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'TylerK',
        'title': 'Blog post 1',
        'content': 'First Blog post content',
        'date_posted': 'December 24, 2020'
    },
        {
        'author': 'Jane',
        'title': 'Blog post 2',
        'content': 'Second Blog post content',
        'date_posted': 'December 27, 2020'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context);

def about(request):
    return render(request, 'blog/about.html');

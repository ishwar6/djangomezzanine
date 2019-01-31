from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
# Create your views here.
import datetime
from .models import Post


def show_post(request):

    q = Post.objects.all()
    print(q)
    print(request.method)
    context = {
        'time': datetime.datetime.now(),
        'posts': q
    }
    return render(request, 'posts/posts.html', context)


def detail(request, post_id):
    q = Post.objects.filter(slug=post_id)
    if q.exists():
        q = q.first()
    else:
        return HttpResponse('<h1>Page Not Found</h1>')

    context = {

        'post': q
    }
    return render(request, 'posts/details.html', context)


def _detail(request, slug):

    q = Post.objects.filter(slug__iexact=slug)
    if q.exists():
        q = q.first()
    else:
        return HttpResponse('<h1>Post Not Found</h1>')
    context = {

        'post': q
    }
    return render(request, 'posts/details.html', context)


def homepage(request):
    return HttpResponse('<h1>Homepage</h1>')

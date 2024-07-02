from typing import Any
from django.shortcuts import render, get_object_or_404
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from blog.data import posts
# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    context = {
        "name": "BLOG",
        "title": "Blog",
        "tema": 'Tema-blog',
        "data": posts
        }
    return render(request, 'blog/home.html',context=context)


def post(request: HttpRequest, pk: int) -> HttpResponse: 
    found_post: dict[str, Any] | None = None
    for item in posts:
        if item['id'] == pk:
            found_post = item
            break

    context = {
        "name": "BLOG",
        "title": f"Post->{item['id']}",
        "tema": 'Tema-post',
        "data": found_post
        }
    
    print(request, pk)
    return render(request, 'blog/post.html', context=context)

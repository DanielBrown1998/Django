from django.shortcuts import render, HttpResponse, get_object_or_404
from blog.data import posts
# Create your views here.

def index(request):
    context = {
        "name": "BLOG",
        "title": "Blog",
        "tema": 'Tema-blog',
        "data": posts
        }
    return render(request, 'blog/home.html',context=context)


def post(request, pk: int):
    for item in posts:
        if item['id'] == pk:
            context = {
                "name": "BLOG",
                "title": f"Post->{item['id']}",
                "tema": 'Tema-post',
                "data": item
                }
    print(request, pk)
    return render(request, 'blog/post.html', context=context)
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        "name": "HOME",
        "title": "Home",
        "tema": "Tema-home",
        "lista": [c for c in range(10)]
        }
    return render(request, 'home/home.html', context=context)


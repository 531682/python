from django.shortcuts import render
from .models import Post

def home(request):
    context = {
        'credentials': Post.objects.all()
    }
    return render(request, 'manager/home.html', context)

def new(request):
    return render(request, 'manager/new.html')

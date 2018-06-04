from django.shortcuts import render

# Create your views here.


def index(request):
    """blog的主页"""
    return render(request, 'blogs/index.html')

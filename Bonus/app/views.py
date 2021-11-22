from django.shortcuts import render
from app.models import *


# Create your views here.
def myfirstview(request):
    data = {
        'name': 'William',
        'categories': Category.objects.all()

    }
    return render(request, 'index.html', data)

def mysecondview(request):
    data = {
        'name': 'William',
        'products': Product.objects.all()

    }
    return render(request, 'seconds.html', data)
    
def mysecondview(request):
    return render(request, 'boot.html')
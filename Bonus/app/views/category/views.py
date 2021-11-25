from django.shortcuts import render
from django.views.generic import ListView
from app.models import *


# Create your views here.
def category_list(request):
    data = {
        'title' : 'Lista de categoria',
        'categories': Category.objects.all()

    }
    return render(request, 'category/list.html', data)

class CategoryListView(ListView):
    model = Category
    template_name  = 'category/list.html'
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title']= 'listado de categoria'
        return context
    
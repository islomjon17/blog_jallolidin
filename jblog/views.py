from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import BlogPost
# Create your views here.



# def home(request):
#     return render(request, 'home.html', {})


class HomeView(ListView):
    model = BlogPost
    template_name = 'home.html'


class ArticleView(DetailView):
    model = BlogPost
    template_name = 'home.html'
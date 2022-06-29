from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import BlogPost
# Create your views here.



# def home(request):
#     return render(request, 'home.html', {})


class HomeView(ListView):
    model = BlogPost
    template_name = 'home.html'


class ArticleDetailsView(DetailView):
    model = BlogPost
    context_object_name = 'post'
    template_name = 'article_details.html'
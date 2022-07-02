from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import BlogPost

from .forms import PostForm, CategoryForm
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
    


class AddPostView(CreateView):
    model = BlogPost
    form_class = PostForm
    template_name = 'add_post.html'
    ordering = ['created_ons']
    # fields = "__all__"

class UpdatePostView(UpdateView):
    model = BlogPost
    form_class = PostForm
    context_object_name = 'post'
    template_name = 'update_post.html'
    # fields = "__all__"


class PostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class AddCategoryView(CreateView):
    model = BlogPost
    form_class = CategoryForm
    template_name = 'add_category.html'
from ast import Return
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from .models import BlogPost, Category

from .forms import PostForm, CategoryForm
# Create your views here.


def LikeView(request, pk):
    post = get_object_or_404(BlogPost, id=request.POST.get('post_id'))

    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))


class HomeView(ListView):
    model = BlogPost
    template_name = 'home.html'


class ArticleDetailsView(DetailView):
    model = BlogPost
    context_object_name = 'post'
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailsView, self).get_context_data(
            *args, **kwargs)

        stuff = get_object_or_404(BlogPost, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes

        return context


def CategoryView(request, cats):
    pk = Category.objects.get(name=cats)
    category_post = BlogPost.objects.filter(category=pk)

    return render(request, 'categories.html', {
        "category_post": category_post})


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

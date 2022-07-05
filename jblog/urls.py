

from django.urls import path, include
from .views import HomeView, CategoryView, LikeView, ArticleDetailsView, AddPostView, UpdatePostView, PostDeleteView, AddCategoryView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailsView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('update_post/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('delete_post/<int:pk>/remove',
         PostDeleteView.as_view(), name='delete_post'),
    path('cats/<str:cats>/', CategoryView, name='category'),
    path('like/<int:pk>', LikeView, name='like_post'),

]

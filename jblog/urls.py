

from django.urls import path, include
from .views import HomeView, ArticleDetailsView, AddPostView, UpdatePostView, PostDeleteView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailsView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('update_post/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('delete_post/<int:pk>/remove', PostDeleteView.as_view(), name='delete_post'),
    
   
]

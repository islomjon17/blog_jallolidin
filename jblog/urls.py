

from django.urls import path, include
from .views import HomeView, ArticleDetailsView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailsView.as_view(), name='article-detail'),
]

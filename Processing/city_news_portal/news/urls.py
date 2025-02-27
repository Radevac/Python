from django.urls import path
from .views import (
    ArticleListCreateView, ArticleDetailView,
    TagListCreateView, CommentListCreateView, CommentDetailView
)

urlpatterns = [
    path('articles/', ArticleListCreateView.as_view(), name='article-list'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('tags/', TagListCreateView.as_view(), name='tag-list'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
]

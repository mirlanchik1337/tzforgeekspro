# urls.py
from django.urls import path
from .views import ArticleListCreate, ArticleDetail, CommentCreate, CommentList

urlpatterns = [
    path('articles/', ArticleListCreate.as_view(), name='article-list-create'),
    path('articles/<int:pk>/', ArticleDetail.as_view(), name='article-detail'),
    path('articles/<int:article_id>/comments/', CommentCreate.as_view(), name='comment-create'),
    path('articles/<int:article_id>/comments/', CommentList.as_view(), name='comment-list'),
]

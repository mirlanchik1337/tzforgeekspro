# views.py
from rest_framework import generics
from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer

class ArticleListCreate(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetail(generics.RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class CommentCreate(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentList(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        article_id = self.kwargs['article_id']
        return Comment.objects.filter(article_id=article_id)

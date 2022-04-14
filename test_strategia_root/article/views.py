from django.shortcuts import render
from rest_framework import generics, permissions

from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer


# Create your views here.
class ArticleReadCreateAPI(generics.ListCreateAPIView):
    """Обрабатывает GET и POST запросы, возвращает все статьи и позволяет создавать новые"""
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.AllowAny, )


class CreateCommentAPI()

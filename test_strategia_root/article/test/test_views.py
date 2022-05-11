import json
from rest_framework import status
from django.urls import include, path
from rest_framework.test import APITestCase, APIRequestFactory
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Article, Comment
from ..views import ArticleReadCreateAPI
from ..serializers import ArticleSerializer, CommentSerializer, ReplyToCommentSerializer


client = Client()


class ArticleTest(APITestCase):
    """Тестирование views статей"""
    api_request_factory = APIRequestFactory()

    def test_get_article_list(self):
        """Получение списка всех статей"""
        view = ArticleReadCreateAPI.as_view()
        request = self.api_request_factory.get('/api/v1/article/')
        print(request)
        response = view(request)
        assert response.status_code == 200

import json
import requests
from rest_framework import status
from django.urls import include, path
from rest_framework.test import APITestCase, APIRequestFactory
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Article, Comment
from ..views import ArticleReadCreateAPI
from ..serializers import ArticleSerializer, CommentSerializer, ReplyToCommentSerializer
from test_strategia.urls import URL, API_URL


client = Client()


class TestArticleReadCreateAPI(APITestCase):
    """Тестирование views статей"""
    factory = APIRequestFactory()

    def setUp(self) -> None:
        self.article_1 = Article.objects.create(
            name='test_name_1',
            description='description',
        )

    def test_check_status_code_200_for_get_article_list(self):
        """Проверка подключения к API для получения списка всех статей"""
        response = requests.get(f'{URL}{API_URL}article/')
        assert response.status_code == 200

    def test_check_content_type_for_get_article_list(self):
        """Проверка типа данных в ответе для получения списка всех статей"""
        response = requests.get(f'{URL}{API_URL}article/')
        assert response.headers['Content-Type'] == 'application/json'

    def test_check_status_code_for_get_article_list(self):
        """Получение списка всех статей"""
        request = self.factory.get(f'{API_URL}article/')
        response = ArticleReadCreateAPI.as_view()(request)
        assert response.status_code == 200

    def test_post_article(self):
        """Проверка создания статьи"""
        response = self.client.get(reverse('article-list'))
        article = Article.objects.all()
        serializer = ArticleSerializer(article, many=True)
        data = dict(response.data)
        data = data['results']
        self.assertEqual(data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.content_type, 'application/json')

        # data = {
        #     'name': 'test_1',
        #     'description': 'description',
        # }
        # response = requests.post(f'{URL}{API_URL}article/', data)
        # assert response.status_code == 201



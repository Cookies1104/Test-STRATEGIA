import requests
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Article, Comment
from ..views import ArticleReadCreateAPI
from ..serializers import ArticleSerializer, CommentSerializer, ReplyToCommentSerializer
from test_strategia.urls import URL, API_URL


client = Client()


class TestArticleReadCreateAPI(APITestCase):
    """Тестирование views статей django test, статические тесты"""
    factory = APIRequestFactory()

    def setUp(self) -> None:
        self.article_1 = Article.objects.create(
            name='test_name_1',
            description='description',
        )
        self.article_2 = Article.objects.create(
            name='test_name_2',
            description='description',
        )

    def test_get_article_list(self):
        """Получение списка всех статей"""
        response = self.client.get(reverse('article-list'))
        article = Article.objects.all()
        serializer = ArticleSerializer(article, many=True)
        data = dict(response.data)['results']

        self.assertEqual(data, serializer.data, 'Данные при получении списка статей не совпадают')
        self.assertEqual(response.status_code, status.HTTP_200_OK, 'Статус ответ не 200')
        self.assertEqual(response.headers['Content-type'], 'application/json', 'Формат ответа не json')

    def test_post_article(self):
        """Проверка создания статьи"""
        data = {'name': 'test_1', 'description': 'description', }
        response = self.client.post(reverse('article-list'), data=data, format='json')
        article = Article.objects.get(name=data['name'])

        self.assertEqual(response.status_code, status.HTTP_201_CREATED, 'Статус ответа не 201')
        self.assertEqual(article.name, data['name'], 'Данные при создании объекта не совпадают')
        self.assertEqual(response.headers['Content-type'], 'application/json', 'Формат ответа не json')


class TestPytestArticleReadCreateAPI(TestCase):
    """Тестирование views статей pytest, динамические тесты"""
    url = f'{URL}{API_URL}article/'

    def test_check_status_code_200_for_get_article_list(self):
        """Проверка подключения к API для получения списка всех статей"""
        response = requests.get(self.url)
        print(response.content)
        assert response.status_code == 200
        assert response.headers['Content-Type'] == 'application/json'
        # assert response.content








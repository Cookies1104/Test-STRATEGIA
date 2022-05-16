import requests
import time
import json
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Article, Comment
from ..views import ArticleReadCreateAPI
from ..serializers import ArticleSerializer, CommentSerializer, ReplyToCommentSerializer
from test_strategia.urls import BASE_URL, API_URL


class TestArticleReadCreateAPI(APITestCase):
    """Тестирование views статей django test, статические тесты"""

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

        self.assertEqual(response.json()['results'], serializer.data, 'Данные при получении списка статей не совпадают')
        self.assertEqual(response.status_code, status.HTTP_200_OK, 'Статус ответ не 200')
        self.assertEqual(response.headers['Content-type'], 'application/json', 'Формат ответа не json')

    def test_post_article(self):
        """Проверка создания статьи"""
        data = {'name': 'test_1', 'description': 'description', }
        response = self.client.post(reverse('article-list'), data=data, format='json')

        article = Article.objects.get(id=response.data['id'])
        serializer = ArticleSerializer(article, many=False)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED, 'Статус ответа при создании статьи не 201')
        self.assertEqual(serializer.data, response.json(), 'Создание статьи в БД не удалось')
        self.assertEqual(response.headers['Content-type'],
                         'application/json',
                         'Форма данных в ответе при создании статьи не соответствует')

    def test_put_article(self):
        """Обновление статьи"""
        data = {'name': 'test_1', 'description': 'description', }
        response_post = self.client.post(reverse('article-list'), data=data, format='json')
        id_ = response_post.data['id']

        new_data = {'name': 'update_test', 'description': 'update description'}
        response_put = self.client.put(reverse('article-one', kwargs={'pk': id_}), data=new_data, )

        article = Article.objects.get(id=response_put.data['id'])
        serializer = ArticleSerializer(article, many=False)

        self.assertEqual(response_post.status_code,
                         status.HTTP_201_CREATED,
                         'Создание статьи для дальнейшего обнновления не удалось')
        self.assertEqual(response_put.status_code, status.HTTP_200_OK, 'Статус ответа при обновлении статьи не 200')
        self.assertEqual(serializer.data, response_put.json(), 'Обновление статьи в БД не удалось')
        self.assertEqual(response_put.headers['Content-type'],
                         'application/json',
                         'Форма данных в ответе при обновлении статьи не соответствует')

    def test_delete_article(self):
        """Удаление статьи"""
        data = {'name': 'test_1', 'description': 'description', }
        response_post = self.client.post(reverse('article-list'), data=data, format='json')
        id_ = response_post.data['id']
        response_delete = self.client.delete(reverse('article-one', kwargs={'pk': id_}))

        self.assertEqual(response_post.status_code,
                         status.HTTP_201_CREATED,
                         'Создание статьи для дальнейшего удаления не удалось')
        self.assertEqual(response_delete.status_code,
                         status.HTTP_204_NO_CONTENT,
                         'При удалении статьи ответа срвера не 204')


class TestPytestArticleReadCreateAPI(TestCase):
    """Тестирование views статей pytest, динамические тесты"""
    url = f'{BASE_URL}{API_URL}article/'

    def _request_post(self):
        data = {'name': 'test_1', 'description': 'description'}
        response = requests.post(self.url, data=data)
        return json.loads(response.content)

    def test_get_article_list(self):
        """Проверка подключения к API для получения списка всех статей"""
        response = requests.get(self.url)
        assert response.status_code == 200
        assert response.headers['Content-Type'] == 'application/json'

    def test_post_article_list(self):
        """Проверка создания статьи"""
        data = {'name': 'test_1', 'description': 'description'}
        response = requests.post(self.url, data=data)
        json_data = json.loads(response.content)
        # article = Article.objects.get(id=json_data['id'])

        assert response.status_code == 201
        assert response.headers['Content-Type'] == 'application/json'
        assert [json_data['name'], json_data['description']] == [data['name'], data['description']]

    # def test_put_article_list(self):
    #     """Проверка обновления статьи"""
    #     data = {'name': 'update_test', 'description': 'update description'}
    #     url = self.url + '/' + str(self.id) + '/'
    #     print(self.id)
    #
    #     response = requests.put(url, data=data)
    #     # json_data = json.loads(response.content)
    #     print(response)
    #
    #     print(response.status_code)
    #     print()
    #     assert response.headers['Content-Type'] == 'application/json'


class TestReadCommentAPI:
    """Тестирование views ReadCommentAPI чтения комментариев"""
    pass












from django.test import TestCase
from ..models import Article, Comment


class ArticleTest(TestCase):
    """Тестирование медели статей"""
    def setUp(self) -> None:
        """Создаём новый объект перед каждым запуском метода"""
        Article.objects.create(
            name='test article',
            description='test description',
        )

    def test_get_article_name(self):
        article = Article.objects.get(name='test article')
        self.assertEqual(article.get_article_name(), 'test article')


class CommentTest(TestCase):
    """Тестирование медели статей"""
    def setUp(self) -> None:
        """Создаём новые объекты перед каждым запуском метода"""
        article = Article.objects.create(
            name='test article',
            description='test description',
        )
        comment = Comment.objects.create(
            text='test comment 1',
            article=article,
            parent=None,
        )
        Comment.objects.create(
            text='test comment 2',
            article=comment.article,
            parent=comment,
            level=comment.level + 1,
        )

    def test_get_article_name(self):
        """Проверка получения имени статьи к которой принадлежит комментарий"""
        comment = Comment.objects.get(text='test comment 1')
        self.assertEqual(comment.get_article(), 'test article')

    def test_get_parent(self):
        """Проверка получения родительского комментария"""
        comment = Comment.objects.get(text='test comment 2')
        self.assertEqual(comment.get_parent_comment(), 'test comment 1')

    def test_get_level_comment(self):
        """Проверка поулчения уровня комментария"""
        comment = Comment.objects.get(text='test comment 2')
        self.assertEqual(comment.get_level_comment(), 2)




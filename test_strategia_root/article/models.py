from django.db import models
from django.conf import settings


# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    create_date = models.DateTimeField(auto_now_add=True, blank=True)
    update_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, )

    def __str__(self):
        return self.name

    def get_article_name(self):
        return self.name

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comment(models.Model):
    text = models.CharField(max_length=1000)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    create_date = models.DateTimeField(auto_now_add=True, blank=True)
    update_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               default=None,
                               null=True,
                               blank=True,
                               related_name='parent_%(class)s',
                               verbose_name='parent comment')
    level = models.IntegerField(default=1, blank=True)
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, )

    def __str__(self):
        return f'Комментарий {self.text}, уровня {self.level} к статье {self.article}'

    def get_parent_comment(self):
        return self.parent.text

    def get_article(self):
        return self.article.name

    def get_level_comment(self):
        return self.level

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

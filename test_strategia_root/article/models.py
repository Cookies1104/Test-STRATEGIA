from django.db import models


# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    create_date = models.DateTimeField(auto_now_add=True, blank=True)
    update_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
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
                               null=True,
                               blank=True,
                               related_name='parent_%(class)s',
                               verbose_name='parent comment')

    def __str__(self):
        return f'Комментарий {self.text} к статье {self.article}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers

from .models import Article, Comment


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'name', 'description', )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'text', 'article', 'level', 'parent', )
        read_only_fields = ('level', 'parent', )


@extend_schema_serializer(exclude_fields=['level', ])
class ReplyToCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'text', 'parent', 'article', 'level', )
        read_only_fields = ['article', ]

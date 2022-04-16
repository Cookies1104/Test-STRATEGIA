from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer, ReplyToCommentSerializer
from .service import checking_primary_key


# Create your views here.
class ArticleReadCreateAPI(generics.ListCreateAPIView):
    """Отображение существующих статей, а также создание новых"""
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.AllowAny, )


class ReadCommentAPI(generics.ListAPIView):
    """Отображение всех комментариев"""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.AllowAny, )


class ReadCommentForArticleAPI(APIView):
    """Отображение комментариев до 3 уровня к конкретной статье"""
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('article_id')
        check = checking_primary_key(model=Article, pk=pk)
        if check is None:
            comment_list = Comment.objects.filter(article=pk, level=3 and 2 and 1)
            return Response({'comments': CommentSerializer(comment_list, many=True).data})
        else:
            return check


class CreateCommentForArticleAPI(APIView):
    """Создание комментария к конкретной статье"""
    def get(self, request):
        comment = Comment.objects.all()[:1]
        return Response({'comments': CommentSerializer(comment, many=True).data})

    def post(self, request):
        serialazer = CommentSerializer(data=request.data)
        serialazer.is_valid(raise_exception=True)
        new_comment = Comment.objects.create(
            text=request.data['text'],
            article_id=request.data['article'],
        )
        return Response({'post': CommentSerializer(new_comment).data})


class CreateReplyToCommentAPI(APIView):
    """Создание комментария в ответ к другому комментарию"""
    def get(self, request):
        comment = Comment.objects.filter(parent=not None)[:1]
        return Response({'comments': ReplyToCommentSerializer(comment, many=True).data})

    def post(self, request):
        serializer = ReplyToCommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if 'parent' in request.data:
            parent = Comment.objects.get(pk=request.data['parent'])
            new_reply = Comment.objects.create(
                text=request.data['text'],
                parent_id=parent.__dict__['id'],
                article_id=parent.__dict__['article_id'],
                level=parent.__dict__['level'] + 1
            )
            return Response({'comments': ReplyToCommentSerializer(new_reply, many=False).data})
        else:
            return Response({'comments': {'parent': 'обязательное поле'}})


class ReadCommentLevelThreeAPI(APIView):
    """Отображение всех ответов к комментарию 3 уровня"""
    def get(self, request, **kwargs):
        pk = kwargs.get('comment_id')
        check = checking_primary_key(model=Comment, pk=pk)
        if check is None:
            comment_list = Comment.objects.filter(parent_id=pk, level=4)
            return Response({'comments': CommentSerializer(comment_list, many=True).data})
        else:
            return check



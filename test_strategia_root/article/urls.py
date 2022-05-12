from django.urls import path

from article.views import (ArticleReadCreateAPI,
                           ReadCommentForArticleAPI,
                           ReadCommentAPI,
                           CreateCommentForArticleAPI,
                           CreateReplyToCommentAPI,
                           ReadCommentLevelThreeAPI,
                           )

urlpatterns = [
    path('article/', ArticleReadCreateAPI.as_view(), name='article-list'),
    path('comments/', ReadCommentAPI.as_view()),
    path('article/<int:article_id>/comments/', ReadCommentForArticleAPI.as_view()),
    path('comment-for-article/', CreateCommentForArticleAPI.as_view()),
    path('reply-comment/', CreateReplyToCommentAPI.as_view()),
    path('reply-comments/<int:comment_id>/', ReadCommentLevelThreeAPI.as_view())
]

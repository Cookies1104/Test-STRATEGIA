from django.urls import path

from article.views import (ArticleReadCreateAPI,
                           ReadCommentForArticleAPI,
                           ReadCommentAPI,
                           CreateCommentForArticleAPI,
                           CreateReplyToCommentAPI,
                           ReadCommentLevelThreeAPI,
                           ArticleDestroyUpdateDeleteAPI,
                           )

urlpatterns = [
    path('article/', ArticleReadCreateAPI.as_view(), name='article-list', ),
    path('article/<int:pk>/', ArticleDestroyUpdateDeleteAPI.as_view(), name='article-one', ),
    path('comments/', ReadCommentAPI.as_view(), name='comment-list', ),
    path('article/<int:article_id>/comments/', ReadCommentForArticleAPI.as_view(), name='read-one-comment', ),
    path('comment-for-article/', CreateCommentForArticleAPI.as_view(), name='create-one-comment', ),
    path('reply-comment/', CreateReplyToCommentAPI.as_view(), name='create-reply-to-comment', ),
    path('reply-comments/<int:comment_id>/', ReadCommentLevelThreeAPI.as_view(), name='read-reply-list', )
]

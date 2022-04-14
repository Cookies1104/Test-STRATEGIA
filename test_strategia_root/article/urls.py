from django.urls import path

from article.views import ArticleReadCreateAPI

urlpatterns = [
    path('/article/', ArticleReadCreateAPI.as_view()),
    path('', ),
]

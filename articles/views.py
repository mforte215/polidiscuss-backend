from articles.models import Article, User
from articles.serializers import ArticleSerializer
from rest_framework import generics
from rest_framework import permissions
from articles.permissions import IsOwnerOrReadOnly
from articles.serializers import UserSerializer
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, OAuth2Authentication


class ArticleList(generics.ListCreateAPIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class UserList(generics.ListAPIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer
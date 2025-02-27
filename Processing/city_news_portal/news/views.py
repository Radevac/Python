from datetime import timedelta
from rest_framework import generics
from .models import SiteSettings
from .serializers import SiteSettingsSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Article, Tag, Comment
from .serializers import ArticleSerializer, TagSerializer, CommentSerializer
from django.utils.timezone import now
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User
from .models import BannedUser

class ArticleListCreateView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ArticleListCreateView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['date_published', 'author', 'tags']
    search_fields = ['title', 'content']
    ordering_fields = ['date_published', 'author']

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentDetailView(generics.RetrieveDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

@api_view(['POST'])
@permission_classes([IsAdminUser])
def ban_user(request, user_id, days):
    user = User.objects.get(id=user_id)
    banned_until = now() + timedelta(days=days)
    BannedUser.objects.update_or_create(user=user, defaults={'banned_until': banned_until})
    return Response({"message": f"Користувача {user.username} заблоковано на {days} днів."})

@api_view(['POST'])
@permission_classes([IsAdminUser])
def unban_user(request, user_id):
    BannedUser.objects.filter(user_id=user_id).delete()
    return Response({"message": f"Користувач {user_id} розблокований."})

class SiteSettingsView(generics.RetrieveUpdateAPIView):
    queryset = SiteSettings.objects.all()
    serializer_class = SiteSettingsSerializer
    lookup_field = "id"


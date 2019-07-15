from .models import Article
from article.serializers import ArticleSerializer
from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.response import Response


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
 
    def list(self, request, *args, **kwargs):
        if(request.user.is_superuser):
            articles = Article.objects.all()
        else:
            author = User.objects.get(username=request.user.username)
            articles = Article.objects.filter(reviewer=author.id)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
        
    def create(self, request, *args, **kwargs):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data["ip_address"] = ip
        author = User.objects.get(username=request.user.username)
        serializer.validated_data["reviewer"] = author
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

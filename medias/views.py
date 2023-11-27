from django.shortcuts import render
from rest_framework import viewsets
from profiles.paginations import CustomPageNumberPagination
from .models import (
    Article,
)
from .serializers import (
    ArticleListSerializer,
    ArticleDetailSerializer
)

# Create your views here.
class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    pagination_class = CustomPageNumberPagination 

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleListSerializer
        else:
            return ArticleDetailSerializer
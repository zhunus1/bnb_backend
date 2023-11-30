from django.shortcuts import render
from rest_framework import viewsets
from modeltranslation.utils import get_language
from profiles.paginations import CustomPageNumberPagination
from .models import (
    Article,
)
from .serializers import (
    ArticleListSerializer,
    ArticleDetailSerializer
)

from .translation import ArticleTranslationOptions


# Create your views here.
class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    pagination_class = CustomPageNumberPagination 

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleListSerializer
        else:
            return ArticleDetailSerializer
    
    def get_queryset(self):
        current_language = get_language()        
        translated_fields = ArticleTranslationOptions.fields  # Add more fields as needed

        # Use the activated language to filter the queryset based on translated fields
        queryset = Article.objects.filter(
            **{
                f"{field}_{''.join(current_language.split('-'))}__isnull": False
                for field in translated_fields
            }
        )
        return queryset
from rest_framework import serializers
from .models import (
   Article,
)


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'id', 
            'title',
            'banner',
            'content',
            'created',
        )


class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'id', 
            'title',
            'banner',
            'content',
            'created',
        )
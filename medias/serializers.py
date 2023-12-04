from rest_framework import serializers
from .models import (
   Article,
   SupportTicket,
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


class SupportTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportTicket
        fields = (
            'name',
            'email',
            'comment',
        )
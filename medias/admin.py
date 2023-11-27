from django.contrib import admin
from .models import (
    Article,
)

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created', 'updated']
    search_fields = ['title']

from modeltranslation.translator import register, TranslationOptions
from django.utils.translation import gettext as _
from .models import (
    Article,
)


@register(Article)
class ArticleTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'content'
    )
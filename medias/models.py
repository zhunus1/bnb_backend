from django.db import models
from django.utils.translation import gettext as _
from .validators import validate_banner

# Create your models here.
class Article(models.Model):
    title = models.CharField(
        max_length = 255, 
        verbose_name = _("Заголовок")
    )

    banner = models.ImageField(
        upload_to = 'articles/', 
        validators = [validate_banner],
        verbose_name = _("Баннер"),
    )

    content = models.TextField(
        verbose_name = "Контент"
    )

    created = models.DateTimeField(
        verbose_name = _("Создано"),
        auto_now_add = True,
    )

    updated = models.DateTimeField(
        verbose_name = _("Обновлено"),
        auto_now = True,
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _("Статья")
        verbose_name_plural = _("Статьи")
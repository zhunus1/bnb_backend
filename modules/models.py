from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class StartUpStage(models.Model):
    name = models.CharField(
        max_length = 63,
        verbose_name = _("Название"),
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
        return str(self.name)
    
    class Meta:
        verbose_name = _("Стадия стартапа")
        verbose_name_plural = _("Стадии стартапа")


class InvestStage(models.Model):
    name = models.CharField(
        max_length = 63,
        verbose_name = _("Название"),
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
        return str(self.name)
    
    class Meta:
        verbose_name = _("Стадия инвестирования")
        verbose_name_plural = _("Стадии инвестирования")


class Industry(models.Model):
    name = models.CharField(
        max_length = 63,
        verbose_name = _("Название"),
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
        return str(self.name)
    
    class Meta:
        verbose_name = _("Индустрия")
        verbose_name_plural = _("Индустрии")


class BussinessModel(models.Model):
    name = models.CharField(
        max_length = 63,
        verbose_name = _("Название"),
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
        return str(self.name)
    
    class Meta:
        verbose_name = _("Бизнес модель")
        verbose_name_plural = _("Бизнес модели")


class Technology(models.Model):
    name = models.CharField(
        max_length = 63,
        verbose_name = _("Название"),
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
        return str(self.name)
    
    class Meta:
        verbose_name =_("Технология")
        verbose_name_plural = _("Технологии")


class SellingModel(models.Model):
    name = models.CharField(
        max_length = 63,
        verbose_name = _("Название"),
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
        return str(self.name)
    
    class Meta:
        verbose_name = _("Модель продаж")
        verbose_name_plural = _("Модели продаж")


class Country(models.Model):
    name = models.CharField(
        max_length = 63,
        verbose_name = _("Название"),
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
        return str(self.name)
    
    class Meta:
        verbose_name = _("Страна")
        verbose_name_plural = _("Страны")


class InnovationMethod(models.Model):
    name = models.CharField(
        max_length = 63,
        verbose_name = _("Название"),
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
        return str(self.name)
    
    class Meta:
        verbose_name = _("Метод инноваций")
        verbose_name_plural = _("Методы инноваций")
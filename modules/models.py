from django.db import models

# Create your models here.
class StartUpStage(models.Model):
    name = models.CharField(
        max_length = 63,
        verbose_name = "Название",
    )

    created = models.DateTimeField(
        verbose_name = "Создано",
        auto_now_add = True,
    )

    updated = models.DateTimeField(
        verbose_name = "Обновлено",
        auto_now = True,
    )

    def __str__(self):
        return str(self.pk)
    
    class Meta:
        verbose_name = "Стадия стартапа"
        verbose_name_plural = "Стадии стартапа"


class Industry(models.Model):
    name = models.CharField(
        max_length = 63,
        verbose_name = "Название",
    )

    created = models.DateTimeField(
        verbose_name = "Создано",
        auto_now_add = True,
    )

    updated = models.DateTimeField(
        verbose_name = "Обновлено",
        auto_now = True,
    )

    def __str__(self):
        return str(self.pk)
    
    class Meta:
        verbose_name = "Индустрия"
        verbose_name_plural = "Индустрии"


class BussinessModel(models.Model):
    name = models.CharField(
        max_length = 63,
        verbose_name = "Название",
    )

    created = models.DateTimeField(
        verbose_name = "Создано",
        auto_now_add = True,
    )

    updated = models.DateTimeField(
        verbose_name = "Обновлено",
        auto_now = True,
    )

    def __str__(self):
        return str(self.pk)
    
    class Meta:
        verbose_name = "Бизнес модель"
        verbose_name_plural = "Бизнес модели"


class Technology(models.Model):
    name = models.CharField(
        max_length = 63,
        verbose_name = "Название",
    )

    created = models.DateTimeField(
        verbose_name = "Создано",
        auto_now_add = True,
    )

    updated = models.DateTimeField(
        verbose_name = "Обновлено",
        auto_now = True,
    )

    def __str__(self):
        return str(self.pk)
    
    class Meta:
        verbose_name = "Технология"
        verbose_name_plural = "Технологии"


class SellingModel(models.Model):
    name = models.CharField(
        max_length = 63,
        verbose_name = "Название",
    )

    created = models.DateTimeField(
        verbose_name = "Создано",
        auto_now_add = True,
    )

    updated = models.DateTimeField(
        verbose_name = "Обновлено",
        auto_now = True,
    )

    def __str__(self):
        return str(self.pk)
    
    class Meta:
        verbose_name = "Модель продаж"
        verbose_name_plural = "Модели продаж"


class Country(models.Model):
    name = models.CharField(
        max_length = 63,
        verbose_name = "Название",
    ) 

    created = models.DateTimeField(
        verbose_name = "Создано",
        auto_now_add = True,
    )

    updated = models.DateTimeField(
        verbose_name = "Обновлено",
        auto_now = True,
    )

    def __str__(self):
        return str(self.pk)
    
    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"


class InnovationMethod(models.Model):
    name = models.CharField(
        max_length = 63,
        verbose_name = "Название",
    ) 

    created = models.DateTimeField(
        verbose_name = "Создано",
        auto_now_add = True,
    )

    updated = models.DateTimeField(
        verbose_name = "Обновлено",
        auto_now = True,
    )

    def __str__(self):
        return str(self.pk)
    
    class Meta:
        verbose_name = "Метод инноваций"
        verbose_name_plural = "Методы инноваций"


class InvestRound(models.Model):
    name = models.CharField(
        max_length = 63,
        verbose_name = "Название",
    ) 

    created = models.DateTimeField(
        verbose_name = "Создано",
        auto_now_add = True,
    )

    updated = models.DateTimeField(
        verbose_name = "Обновлено",
        auto_now = True,
    )

    def __str__(self):
        return str(self.pk)
    
    class Meta:
        verbose_name = "Раунд инвестиций"
        verbose_name_plural = "Раунды инвестиций"
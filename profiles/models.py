import datetime
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from djmoney.models.fields import MoneyField
from django.core.validators import (
    MaxValueValidator, 
    MinValueValidator
)
from .validators import (
    validate_image,
    validate_presentation
)

def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)  

class InformationSource(models.TextChoices):
        FRIENDS = "Друзья", "Друзья"
        KITH = "Знакомые", "Знакомые"
        FAMILY = "Семья", "Семья"
        SOCIAL = "Социальные сети", "Социальные сети"
        ADVERT = "Реклама в интернете", "Реклама в интернете"
        EMAIL = "Рассылка через почту", "Рассылка через почту"

class AnswersToQuestion(models.TextChoices):
        YES = "Да", "Да"
        NO = "Нет", "Нет"

# Create your models here.
class PilotProject(models.Model):
    title = models.CharField(
        max_length = 63,
        verbose_name = "Название",
    )
    description = models.TextField(
        verbose_name = "Описание",
    )
    content_type = models.ForeignKey(
        ContentType, 
        on_delete=models.CASCADE
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey(
        "content_type", 
        "object_id"
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
        return str(self.title)
    
    class Meta:
        indexes = [
            models.Index(
                fields = [
                    "content_type", 
                    "object_id"
                ]
            ),
        ]
        verbose_name = "Пилотный проект"
        verbose_name_plural = "Пилотные проекты"


class StartUp(models.Model):
    is_approved = models.BooleanField(
        default = False,
        verbose_name = "Прошло проверку?",
    )
    user = models.OneToOneField(
        'users.AppUser', 
        on_delete = models.CASCADE,
        verbose_name = "Пользователь",
    )
    startup_name = models.CharField(
        max_length = 63,
        verbose_name = "Публичное название",
    )
    website = models.URLField(
        verbose_name = "Веб-сайт",
    ) 
    contact_name = models.CharField(
        max_length = 63,
        verbose_name = "Контактное лицо",
    )
    email = models.EmailField(
        verbose_name = "Электронная почта",
    )
    phone = PhoneNumberField(
        verbose_name = "Номер телефона",
    )
    organization_name = models.CharField(
        max_length = 63,
        verbose_name = "Название организации",
    )
    organization_id = models.CharField(
        max_length = 63,
        verbose_name = "Идентификационный номер",
    )
    organization_year = models.IntegerField(
        validators = [
            MinValueValidator(1984), 
            max_value_current_year
        ]
    )
    employees_count = models.PositiveIntegerField(
        verbose_name = "Количество сотрудников",
    )
    description = models.TextField(
        verbose_name = "Описание",
    )
    stage = models.ForeignKey(
        'modules.StartUpStage', 
        on_delete = models.CASCADE,
        related_name = 'startups',
        verbose_name = "Стадия",
    )
    industries = models.ManyToManyField(
        'modules.Industry', 
        related_name = 'startups',
        verbose_name = "Индустрии",
    )
    technologies = models.ManyToManyField(
        'modules.Technology', 
        related_name = 'startups',
        verbose_name = "Технологии",
    )
    bussiness_models = models.ManyToManyField(
        'modules.BussinessModel', 
        related_name = 'startups',
        verbose_name = "Бизнес модели",
    )
    selling_models = models.ManyToManyField(
        'modules.SellingModel', 
        related_name = 'startups',
        verbose_name = "Модели продаж",
    )
    countries = models.ManyToManyField(
        'modules.Country', 
        related_name = 'startups',
        verbose_name = "Страны",
    )
    have_sellings = models.CharField(
        max_length = 3, 
        choices=AnswersToQuestion.choices,
        verbose_name = "Есть продажи?",
    )
    have_pilots = models.CharField(
        max_length = 3, 
        choices=AnswersToQuestion.choices,
        verbose_name = "Есть успешные пилоты?",
    )
    active_search = models.CharField(
        max_length = 3, 
        choices=AnswersToQuestion.choices,
        verbose_name = "В поиске инвестиций?",
    )
    invested_sum = MoneyField(
        max_digits = 12, 
        decimal_places = 0, 
        default_currency = 'USD',
        verbose_name = "Привлечено",
    )
    investors = models.TextField(
        verbose_name = "Инвесторы",
    )
    logo = models.ImageField(
        upload_to = 'start-up/logos/', 
        height_field = '1200', 
        width_field = '1200',
        validators = [validate_image],
        verbose_name = "Логотип",
    )
    presentation = models.FileField(
        upload_to = 'presentations/', 
        validators = [validate_presentation],
        verbose_name = "Презентация",
    )
    information_source = models.CharField(
        max_length = 20, 
        choices = InformationSource.choices,
        verbose_name = "Откуда узнали?",
    )
    views = models.PositiveIntegerField(
        default = 0,
        verbose_name = "Количество просмотров",
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
        return str(self.title)

    def update_views(self, *args, **kwargs):
         self.views = self.views + 1
         super(StartUp, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = "Стартап"
        verbose_name_plural = "Стартапы"


class Investor(models.Model):
    is_approved = models.BooleanField(
        default = False,
        verbose_name = "Прошло проверку?",
    )
    user = models.OneToOneField(
        'users.AppUser', 
        on_delete = models.CASCADE,
        verbose_name = "Пользователь",
    )
    contact_name = models.CharField(
        max_length = 63,
        verbose_name = "Контактное лицо",
    )
    email = models.EmailField(
        verbose_name = "Электронная почта",
    )
    phone = PhoneNumberField(
        verbose_name = "Номер телефона",
    )
    country = models.ForeignKey(
        'modules.Country', 
        on_delete = models.CASCADE,
        related_name = 'country_investors',
        verbose_name = "Страна регистрации",
    )
    description = models.TextField(
        verbose_name = "Описание",
    )
    information_source = models.CharField(
        max_length = 20, 
        choices = InformationSource.choices,
        verbose_name = "Откуда узнали?",
    )
    invest_sum = MoneyField(
        max_digits = 12, 
        decimal_places = 0, 
        default_currency = 'USD',
        verbose_name = "Размер средств",
    )
    methods = models.ManyToManyField(
        'modules.InnovationMethod', 
        related_name = 'investors',
        verbose_name = "Методы работы",
    )
    stage = models.ManyToManyField(
        'modules.StartUpStage', 
        related_name = 'investors',
        verbose_name = "Релевантные стадии",
    )
    technologies = models.ManyToManyField(
        'modules.Technology', 
        related_name = 'investors',
        verbose_name = "Релевантные технологии",
    )
    industries = models.ManyToManyField(
        'modules.Industry', 
        related_name = 'investors',
        verbose_name = "Релевантные индустрии",
    )
    have_experience = models.CharField(
        max_length = 3, 
        choices=AnswersToQuestion.choices,
        verbose_name = "Опыт пилотирования?",
    )
    is_investing = models.CharField(
        max_length = 3, 
        choices=AnswersToQuestion.choices,
        verbose_name = "Инвистирует?",
    )
    invest_rounds = models.ManyToManyField(
        'modules.InvestRound', 
        related_name = 'investors',
        verbose_name = "Раунды инвестиций",
    )
    geography = models.ManyToManyField(
        'modules.Country', 
        related_name = 'geography_investors',
        verbose_name = "География стартапов",
    )
    views = models.PositiveIntegerField(
        default = 0,
        verbose_name = "Количество просмотров",
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

    def update_views(self, *args, **kwargs):
         self.views = self.views + 1
         super(StartUp, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = "Инвестор"
        verbose_name_plural = "Инвесторы"


class InvestFund(models.Model):
    is_approved = models.BooleanField(
        default = False,
        verbose_name = "Прошло проверку?",
    )
    user = models.OneToOneField(
        'users.AppUser', 
        on_delete = models.CASCADE,
        verbose_name = "Пользователь",
    )
    public_name = models.CharField(
        max_length = 63,
        verbose_name = "Публичное название",
    )
    contact_name = models.CharField(
        max_length = 63,
        verbose_name = "Контактное лицо",
    )
    email = models.EmailField(
        verbose_name = "Электронная почта",
    )
    phone = PhoneNumberField(
        verbose_name = "Номер телефона",
    )
    organization_name = models.CharField(
        max_length = 63,
        verbose_name = "Наименование организации",
    )
    organization_id = models.CharField(
        max_length = 63,
        verbose_name = "Идентификационный номер",
    )
    country = models.ForeignKey(
        'modules.Country', 
        on_delete = models.CASCADE,
        related_name = 'country_invest_funds',
        verbose_name = "Страна регистрации",
    )
    website = models.URLField(
        verbose_name = "Веб-сайт",
    )
    description = models.TextField(
        verbose_name = "Описание",
    )
    logo = models.ImageField(
        upload_to = 'invest-funds/logos/', 
        height_field = '1200', 
        width_field = '1200',
        validators = [validate_image],
        verbose_name = "Логотип",
    )
    information_source = models.CharField(
        max_length = 20, 
        choices = InformationSource.choices,
        verbose_name = "Откуда узнали?",
    )
    invest_sum = MoneyField(
        max_digits = 12, 
        decimal_places = 0, 
        default_currency = 'USD',
        verbose_name = "Размер средств",
    )
    methods = models.ManyToManyField(
        'modules.InnovationMethod', 
        related_name = 'invest_funds',
        verbose_name = "Методы работы",
    )
    stage = models.ManyToManyField(
        'modules.StartUpStage', 
        related_name = 'invest_funds',
        verbose_name = "Релевантные стадии",
    )
    technologies = models.ManyToManyField(
        'modules.Technology', 
        related_name = 'invest_funds',
        verbose_name = "Релевантные технологии",
    )
    industries = models.ManyToManyField(
        'modules.Industry', 
        related_name = 'invest_funds',
        verbose_name = "Релевантные индустрии",
    )
    have_experience = models.CharField(
        max_length = 3, 
        choices=AnswersToQuestion.choices,
        verbose_name = "Опыт пилотирования?",
    )
    is_investing = models.CharField(
        max_length = 3, 
        choices=AnswersToQuestion.choices,
        verbose_name = "Инвистирует?",
    )
    invest_rounds = models.ManyToManyField(
        'modules.InvestRound', 
        related_name = 'invest_funds',
        verbose_name = "Раунды инвестиций",
    )
    geography = models.ManyToManyField(
        'modules.Country', 
        related_name = 'geography_invest_funds',
        verbose_name = "География стартапов",
    )
    views = models.PositiveIntegerField(
        default = 0,
        verbose_name = "Количество просмотров",
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

    def update_views(self, *args, **kwargs):
         self.views = self.views + 1
         super(StartUp, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = "Инвестиционный фонд"
        verbose_name_plural = "Инвестиционные фонды"


class Corporation(models.Model):
    is_approved = models.BooleanField(
        default = False,
        verbose_name = "Прошло проверку?",
    )
    user = models.OneToOneField(
        'users.AppUser', 
        on_delete = models.CASCADE,
        verbose_name = "Пользователь",
    )
    public_name = models.CharField(
        max_length = 63,
        verbose_name = "Публичное название",
    )
    email = models.EmailField(
        verbose_name = "Электронная почта",
    )
    organization_name = models.CharField(
        max_length = 63,
        verbose_name = "Наименование организации",
    )
    organization_id = models.CharField(
        max_length = 63,
        verbose_name = "Идентификационный номер",
    )
    country = models.ForeignKey(
        'modules.Country', 
        on_delete = models.CASCADE,
        related_name = 'country_corporations',
        verbose_name = "Страна регистрации",
    )
    website = models.URLField(
        verbose_name = "Ссылка на веб-сайт",
    )
    description = models.TextField(
        verbose_name = "Описание",
    )
    logo = models.ImageField(
        upload_to = 'corporations/logos/', 
        height_field = '1200', 
        width_field = '1200',
        validators = [validate_image],
        verbose_name = "Логотип",
    )
    information_source = models.CharField(
        max_length = 20, 
        choices = InformationSource.choices,
        verbose_name = "Откуда узнали?",
    )
    methods = models.ManyToManyField(
        'modules.InnovationMethod', 
        related_name = 'corporations',
        verbose_name = "Методы работы",
    )
    stage = models.ManyToManyField(
        'modules.StartUpStage', 
        related_name = 'corporations',
        verbose_name = "Релевантные стадии",
    )
    technologies = models.ManyToManyField(
        'modules.Technology', 
        related_name = 'corporations',
        verbose_name = "Релевантные технологии",
    )
    industries = models.ManyToManyField(
        'modules.Industry', 
        related_name = 'corporations',
        verbose_name = "Релевантные индустрии",
    )
    have_experience = models.CharField(
        max_length = 3, 
        choices=AnswersToQuestion.choices,
        verbose_name = "Опыт пилотирования?",
    )
    is_investing = models.CharField(
        max_length = 3, 
        choices=AnswersToQuestion.choices,
        verbose_name = "Инвистирует?",
    )
    invest_rounds = models.ManyToManyField(
        'modules.InvestRound', 
        related_name = 'corporations',
        verbose_name = "Раунды инвестиций",
    )
    geography = models.ManyToManyField(
        'modules.Country', 
        related_name = 'geography_corporations',
        verbose_name = "География стартапов",
    )
    views = models.PositiveIntegerField(
        default = 0,
        verbose_name = "Количество просмотров",
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
    
    def update_views(self, *args, **kwargs):
         self.views = self.views + 1
         super(StartUp, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = "Корпорация"
        verbose_name_plural = "Корпорации"


class Specialist(models.Model):
    is_approved = models.BooleanField(
        default = False,
        verbose_name = "Прошло проверку?",
    )
    user = models.OneToOneField(
        'users.AppUser', 
        on_delete = models.CASCADE,
        verbose_name = "Пользователь",
    )
    experience = models.TextField(
        verbose_name = "Опыт работы",
    )
    industries = models.ManyToManyField(
        'modules.Industry', 
        related_name = 'specialists',
        verbose_name = "Релевантные индустрии",
    )
    technologies = models.ManyToManyField(
        'modules.Technology', 
        related_name = 'specialists',
        verbose_name = "Релевантные технологии",
    )
    profile_image = models.ImageField(
        upload_to = 'profiles/images/', 
        height_field = '1200', 
        width_field = '1200',
        validators = [validate_image],
        verbose_name = "Фото профиля",
    )
    resume = models.FileField(
        upload_to = 'profiles/resumes/', 
        validators = [validate_presentation],
        verbose_name = "Резюме",
    )
    information_source = models.CharField(
        max_length = 20, 
        choices = InformationSource.choices,
        verbose_name = "Откуда узнали?",
    )
    views = models.PositiveIntegerField(
        default = 0,
        verbose_name = "Количество просмотров",
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
    
    def update_views(self, *args, **kwargs):
         self.views = self.views + 1
         super(StartUp, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = "Специалист"
        verbose_name_plural = "Специалисты"
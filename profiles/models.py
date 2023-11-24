import datetime
from django.db import models
from django.utils.translation import gettext as _
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
        FRIENDS = "Друзья", _("Друзья")
        KITH = "Знакомые", _("Знакомые")
        FAMILY = "Семья", _("Семья")
        SOCIAL = "Социальные сети", _("Социальные сети")
        ADVERT = "Реклама в интернете", _("Реклама в интернете")
        EMAIL = "Рассылка через почту", _("Рассылка через почту")

class AnswersToQuestion(models.TextChoices):
        YES = "Да", _("Да")
        NO = "Нет", _("Нет")

class WorkExperience(models.TextChoices):
        NO_EXP = "Нет опыта", _("Нет опыта")
        JUNIOR = "1-3 года", _("1-3 года")
        MIDLE = "3-6 года", _("3-6 года")
        SENIOR = "6+ лет", _("6+ лет")

# Create your models here.
class PilotProject(models.Model):
    title = models.CharField(
        max_length = 63,
        verbose_name = _("Название"),
    )
    description = models.TextField(
        verbose_name = _("Описание"),
    )
    content_type = models.ForeignKey(
        ContentType, 
        on_delete = models.CASCADE
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey(
        "content_type", 
        "object_id"
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
        verbose_name = _("Пилотный проект")
        verbose_name_plural = _("Пилотные проекты")


class StartUp(models.Model):
    is_approved = models.BooleanField(
        default = False,
        verbose_name = _("Прошло проверку?"),
    )
    user = models.OneToOneField(
        'users.AppUser', 
        on_delete = models.CASCADE,
        verbose_name = _("Пользователь"),
    )
    startup_name = models.CharField(
        max_length = 63,
        verbose_name = _("Публичное название"),
    )
    website = models.URLField(
        verbose_name = _("Веб-сайт"),
    ) 
    contact_name = models.CharField(
        max_length = 63,
        verbose_name = _("Контактное лицо"),
    )
    email = models.EmailField(
        verbose_name = _("Электронная почта"),
    )
    phone = PhoneNumberField(
        verbose_name = _("Номер телефона"),
    )
    organization_name = models.CharField(
        max_length = 63,
        verbose_name =_("Название организации"),
    )
    organization_id = models.CharField(
        max_length = 63,
        verbose_name = _("Идентификационный номер"),
    )
    organization_year = models.IntegerField(
        validators = [
            MinValueValidator(1984), 
            max_value_current_year
        ]
    )
    employees_count = models.PositiveIntegerField(
        verbose_name = _("Количество сотрудников"),
    )
    description = models.TextField(
        verbose_name = _("Описание"),
    )
    startup_stage = models.ForeignKey(
        'modules.StartUpStage', 
        on_delete = models.CASCADE,
        related_name = 'startups',
        verbose_name = _("Стадия стартапа"),
    )
    invest_stage = models.ForeignKey(
        'modules.InvestStage', 
        on_delete = models.CASCADE,
        related_name = 'startups',
        verbose_name = _("Стадия инвестирования"),
    )
    industries = models.ManyToManyField(
        'modules.Industry', 
        related_name = 'startups',
        verbose_name = _("Индустрии"),
    )
    technologies = models.ManyToManyField(
        'modules.Technology', 
        related_name = 'startups',
        verbose_name = _("Технологии"),
    )
    bussiness_models = models.ManyToManyField(
        'modules.BussinessModel', 
        related_name = 'startups',
        verbose_name = _("Бизнес модели"),
    )
    selling_models = models.ManyToManyField(
        'modules.SellingModel', 
        related_name = 'startups',
        verbose_name = _("Модели продаж"),
    )
    countries = models.ManyToManyField(
        'modules.Country', 
        related_name = 'startups',
        verbose_name = _("Страны"),
    )
    have_sellings = models.CharField(
        max_length = 3, 
        choices=AnswersToQuestion.choices,
        verbose_name = _("Есть продажи?"),
    )
    have_pilots = models.CharField(
        max_length = 3, 
        choices=AnswersToQuestion.choices,
        verbose_name = _("Есть успешные пилоты?"),
    )
    active_search = models.CharField(
        max_length = 3, 
        choices=AnswersToQuestion.choices,
        verbose_name = _("В поиске инвестиций?"),
    )
    invested_sum = MoneyField(
        max_digits = 12, 
        decimal_places = 0, 
        default_currency = 'USD',
        verbose_name = _("Привлечено"),
    )
    investors = models.TextField(
        verbose_name = _("Инвесторы"),
    )
    logo = models.ImageField(
        upload_to = 'start-up/logos/', 
        validators = [validate_image],
        verbose_name = _("Логотип"),
    )
    presentation = models.FileField(
        upload_to = 'presentations/', 
        validators = [validate_presentation],
        verbose_name = _("Презентация"),
    )
    information_source = models.CharField(
        max_length = 20, 
        choices = InformationSource.choices,
        verbose_name = _("Откуда узнали?"),
    )
    views = models.PositiveIntegerField(
        default = 0,
        verbose_name = _("Количество просмотров"),
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
        return str(self.startup_name)

    def update_views(self, *args, **kwargs):
         self.views = self.views + 1
         super(StartUp, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = _("Стартап")
        verbose_name_plural = _("Стартапы")


class Investor(models.Model):
    is_approved = models.BooleanField(
        default = False,
        verbose_name = _("Прошло проверку?"),
    )
    user = models.OneToOneField(
        'users.AppUser', 
        on_delete = models.CASCADE,
        verbose_name = _("Пользователь"),
    )
    contact_name = models.CharField(
        max_length = 63,
        verbose_name = _("Контактное лицо"),
    )
    email = models.EmailField(
        verbose_name = _("Электронная почта"),
    )
    phone = PhoneNumberField(
        verbose_name = _("Номер телефона"),
    )
    profile_image = models.ImageField(
        upload_to = 'investors/profiles/images/', 
        validators = [validate_image],
        verbose_name = _("Фото профиля"),
    )
    country = models.ForeignKey(
        'modules.Country', 
        on_delete = models.CASCADE,
        related_name = 'country_investors',
        verbose_name = _("Страна регистрации"),
    )
    description = models.TextField(
        verbose_name = _("Описание"),
    )
    information_source = models.CharField(
        max_length = 20, 
        choices = InformationSource.choices,
        verbose_name = _("Откуда узнали?"),
    )
    invest_sum = MoneyField(
        max_digits = 12, 
        decimal_places = 0, 
        default_currency = 'USD',
        verbose_name = _("Размер средств"),
    )
    methods = models.ManyToManyField(
        'modules.InnovationMethod', 
        related_name = 'investors',
        verbose_name = _("Методы работы"),
    )
    stage = models.ManyToManyField(
        'modules.StartUpStage', 
        related_name = 'investors',
        verbose_name = _("Релевантные стадии"),
    )
    technologies = models.ManyToManyField(
        'modules.Technology', 
        related_name = 'investors',
        verbose_name = _("Релевантные технологии"),
    )
    industries = models.ManyToManyField(
        'modules.Industry', 
        related_name = 'investors',
        verbose_name = _("Релевантные индустрии"),
    )
    have_experience = models.CharField(
        max_length = 3, 
        choices=AnswersToQuestion.choices,
        verbose_name = _("Опыт пилотирования?"),
    )
    is_investing = models.CharField(
        max_length = 3, 
        choices=AnswersToQuestion.choices,
        verbose_name = _("Инвистирует?"),
    )
    invest_rounds = models.ManyToManyField(
        'modules.InvestRound', 
        related_name = 'investors',
        verbose_name = _("Раунды инвестиций"),
    )
    geography = models.ManyToManyField(
        'modules.Country', 
        related_name = 'geography_investors',
        verbose_name = _("География стартапов"),
    )
    views = models.PositiveIntegerField(
        default = 0,
        verbose_name = _("Количество просмотров"),
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
        return str(self.contact_name)

    def update_views(self, *args, **kwargs):
         self.views = self.views + 1
         super(Investor, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = _("Инвестор")
        verbose_name_plural = _("Инвесторы")


class InvestFund(models.Model):
    is_approved = models.BooleanField(
        default = False,
        verbose_name = _("Прошло проверку?"),
    )
    user = models.OneToOneField(
        'users.AppUser', 
        on_delete = models.CASCADE,
        verbose_name = _("Пользователь"),
    )
    public_name = models.CharField(
        max_length = 63,
        verbose_name = _("Публичное название"),
    )
    contact_name = models.CharField(
        max_length = 63,
        verbose_name = _("Контактное лицо"),
    )
    email = models.EmailField(
        verbose_name = _("Электронная почта"),
    )
    phone = PhoneNumberField(
        verbose_name = _("Номер телефона"),
    )
    organization_name = models.CharField(
        max_length = 63,
        verbose_name = _("Наименование организации"),
    )
    organization_id = models.CharField(
        max_length = 63,
        verbose_name = _("Идентификационный номер"),
    )
    country = models.ForeignKey(
        'modules.Country', 
        on_delete = models.CASCADE,
        related_name = 'country_invest_funds',
        verbose_name = _("Страна регистрации"),
    )
    website = models.URLField(
        verbose_name = _("Веб-сайт"),
    )
    description = models.TextField(
        verbose_name = _("Описание"),
    )
    logo = models.ImageField(
        upload_to = 'invest-funds/logos/', 
        validators = [validate_image],
        verbose_name = _("Логотип"),
    )
    information_source = models.CharField(
        max_length = 20, 
        choices = InformationSource.choices,
        verbose_name = _("Откуда узнали?"),
    )
    invest_sum = MoneyField(
        max_digits = 12, 
        decimal_places = 0, 
        default_currency = 'USD',
        verbose_name = _("Размер средств"),
    )
    methods = models.ManyToManyField(
        'modules.InnovationMethod', 
        related_name = 'invest_funds',
        verbose_name = _("Методы работы"),
    )
    stage = models.ManyToManyField(
        'modules.StartUpStage', 
        related_name = 'invest_funds',
        verbose_name = _("Релевантные стадии"),
    )
    technologies = models.ManyToManyField(
        'modules.Technology', 
        related_name = 'invest_funds',
        verbose_name = _("Релевантные технологии"),
    )
    industries = models.ManyToManyField(
        'modules.Industry', 
        related_name = 'invest_funds',
        verbose_name = _("Релевантные индустрии"),
    )
    have_experience = models.CharField(
        max_length = 3, 
        choices=AnswersToQuestion.choices,
        verbose_name = _("Опыт пилотирования?"),
    )
    is_investing = models.CharField(
        max_length = 3, 
        choices=AnswersToQuestion.choices,
        verbose_name = _("Инвистирует?"),
    )
    invest_rounds = models.ManyToManyField(
        'modules.InvestRound', 
        related_name = 'invest_funds',
        verbose_name = _("Раунды инвестиций"),
    )
    geography = models.ManyToManyField(
        'modules.Country', 
        related_name = 'geography_invest_funds',
        verbose_name = _("География стартапов"),
    )
    views = models.PositiveIntegerField(
        default = 0,
        verbose_name = _("Количество просмотров"),
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
        return str(self.public_name)

    def update_views(self, *args, **kwargs):
         self.views = self.views + 1
         super(InvestFund, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = _("Инвестиционный фонд")
        verbose_name_plural = _("Инвестиционные фонды")


class Corporation(models.Model):
    is_approved = models.BooleanField(
        default = False,
        verbose_name = _("Прошло проверку?"),
    )
    user = models.OneToOneField(
        'users.AppUser', 
        on_delete = models.CASCADE,
        verbose_name = _("Пользователь"),
    )
    public_name = models.CharField(
        max_length = 63,
        verbose_name = _("Публичное название"),
    )
    email = models.EmailField(
        verbose_name = _("Электронная почта"),
    )
    organization_name = models.CharField(
        max_length = 63,
        verbose_name = _("Наименование организации"),
    )
    organization_id = models.CharField(
        max_length = 63,
        verbose_name = _("Идентификационный номер"),
    )
    country = models.ForeignKey(
        'modules.Country', 
        on_delete = models.CASCADE,
        related_name = 'country_corporations',
        verbose_name = _("Страна регистрации"),
    )
    website = models.URLField(
        verbose_name = _("Ссылка на веб-сайт"),
    )
    description = models.TextField(
        verbose_name = _("Описание"),
    )
    logo = models.ImageField(
        upload_to = 'corporations/logos/', 
        validators = [validate_image],
        verbose_name = _("Логотип"),
    )
    information_source = models.CharField(
        max_length = 20, 
        choices = InformationSource.choices,
        verbose_name = _("Откуда узнали?"),
    )
    methods = models.ManyToManyField(
        'modules.InnovationMethod', 
        related_name = 'corporations',
        verbose_name = _("Методы работы"),
    )
    stage = models.ManyToManyField(
        'modules.StartUpStage', 
        related_name = 'corporations',
        verbose_name = _("Релевантные стадии"),
    )
    technologies = models.ManyToManyField(
        'modules.Technology', 
        related_name = 'corporations',
        verbose_name = _("Релевантные технологии"),
    )
    industries = models.ManyToManyField(
        'modules.Industry', 
        related_name = 'corporations',
        verbose_name = _("Релевантные индустрии"),
    )
    have_experience = models.CharField(
        max_length = 3, 
        choices=AnswersToQuestion.choices,
        verbose_name = _("Опыт пилотирования?"),
    )
    is_investing = models.CharField(
        max_length = 3, 
        choices=AnswersToQuestion.choices,
        verbose_name = _("Инвистирует?"),
    )
    invest_rounds = models.ManyToManyField(
        'modules.InvestRound', 
        related_name = 'corporations',
        verbose_name = _("Раунды инвестиций"),
    )
    geography = models.ManyToManyField(
        'modules.Country', 
        related_name = 'geography_corporations',
        verbose_name = _("География стартапов"),
    )
    views = models.PositiveIntegerField(
        default = 0,
        verbose_name = _("Количество просмотров"),
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
        return str(self.public_name)
    
    def update_views(self, *args, **kwargs):
         self.views = self.views + 1
         super(Corporation, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = _("Корпорация")
        verbose_name_plural = _("Корпорации")


class Specialist(models.Model):
    is_approved = models.BooleanField(
        default = False,
        verbose_name = _("Прошло проверку?"),
    )
    user = models.OneToOneField(
        'users.AppUser', 
        on_delete = models.CASCADE,
        verbose_name = _("Пользователь"),
    )
    experience = models.TextField(
        verbose_name = _("Описание опыта"),
    )
    experience_years = models.CharField(
        max_length = 9, 
        choices = WorkExperience.choices,
        verbose_name = _("Опыт работы"),
    )
    industries = models.ManyToManyField(
        'modules.Industry', 
        related_name = 'specialists',
        verbose_name = _("Релевантные индустрии"),
    )
    technologies = models.ManyToManyField(
        'modules.Technology', 
        related_name = 'specialists',
        verbose_name = _("Релевантные технологии"),
    )
    profile_image = models.ImageField(
        upload_to = 'specialists/profiles/images/', 
        validators = [validate_image],
        verbose_name = _("Фото профиля"),
    )
    resume = models.FileField(
        upload_to = 'specialists/profiles/resumes/', 
        validators = [validate_presentation],
        verbose_name = _("Резюме"),
    )
    information_source = models.CharField(
        max_length = 20, 
        choices = InformationSource.choices,
        verbose_name = _("Откуда узнали?"),
    )
    views = models.PositiveIntegerField(
        default = 0,
        verbose_name = _("Количество просмотров"),
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
        return str(self.user.name)
    
    def update_views(self, *args, **kwargs):
         self.views = self.views + 1
         super(Specialist, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = _("Специалист")
        verbose_name_plural = _("Специалисты")
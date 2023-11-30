from modeltranslation.translator import register, TranslationOptions
from .models import (
    StartUpStage, 
    Industry, 
    BussinessModel, 
    Technology, 
    SellingModel, 
    Country, 
    InnovationMethod, 
    InvestStage
)


@register(StartUpStage)
class StartUpStageTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )


@register(Industry)
class IndustryTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )


@register(BussinessModel)
class BussinessModelTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )


@register(Technology)
class TechnologyTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )


@register(SellingModel)
class SellingModelTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )


@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )


@register(InnovationMethod)
class InnovationMethodModelTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )


@register(InvestStage)
class InvestStageTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )
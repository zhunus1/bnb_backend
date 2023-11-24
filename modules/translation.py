from modeltranslation.translator import translator, TranslationOptions
from .models import (
    StartUpStage,
    Industry,
    BussinessModel,
    Technology,
    SellingModel,
    Country,
    InnovationMethod,
    InvestRound
)


class StartUpStageTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )
translator.register(StartUpStage, StartUpStageTranslationOptions)


class IndustryTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )
translator.register(Industry, IndustryTranslationOptions)

class BussinessModelTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )
translator.register(BussinessModel, BussinessModelTranslationOptions)


class TechnologyTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )
translator.register(Technology, TechnologyTranslationOptions)


class SellingModelTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )
translator.register(SellingModel, SellingModelTranslationOptions)


class CountryTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )
translator.register(Country, CountryTranslationOptions)


class InnovationMethodTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )
translator.register(InnovationMethod, InnovationMethodTranslationOptions)


class InvestRoundTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )
translator.register(InvestRound, InvestRoundTranslationOptions)
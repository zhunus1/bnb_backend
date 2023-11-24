from modeltranslation.translator import translator, TranslationOptions
from .models import (
    PilotProject,
    StartUp,
    Investor,
    InvestFund,
    Corporation,
    Specialist,
)


class PilotProjectTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'description',
    )
translator.register(PilotProject, PilotProjectTranslationOptions)


class StartUpTranslationOptions(TranslationOptions):
    fields = (
        'startup_name',
        'contact_name',
        'organization_name',
        'description',
        'investors',
    )
translator.register(StartUp, StartUpTranslationOptions)


class InvestorTranslationOptions(TranslationOptions):
    fields = (
        'contact_name',
        'description',
    )
translator.register(Investor, InvestorTranslationOptions)


class InvestFundTranslationOptions(TranslationOptions):
    fields = (
        'public_name',
        'contact_name',
        'organization_name',
        'description',
    )
translator.register(InvestFund, InvestFundTranslationOptions)


class CorporationTranslationOptions(TranslationOptions):
    fields = (
        'public_name',
        'organization_name',
        'description',
    )
translator.register(Corporation, CorporationTranslationOptions)


class SpecialistTranslationOptions(TranslationOptions):
    fields = (
        'experience',
    )
translator.register(Specialist, SpecialistTranslationOptions)
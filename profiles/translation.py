from modeltranslation.translator import register, TranslationOptions
from .models import (
   PilotProject,
   StartUp,
   Investor,
   InvestFund,
   Corporation,
   Specialist,
)


@register(PilotProject)
class PilotProjectTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'description',
    )


@register(StartUp)
class StartUpTranslationOptions(TranslationOptions):
    fields = (
        'startup_name',
        'contact_name',
        'organization_name',
        'description',
        'investors',
    )


@register(Investor)
class InvestorTranslationOptions(TranslationOptions):
    fields = (
        'contact_name',
        'description',
    )


@register(InvestFund)
class InvestFundTranslationOptions(TranslationOptions):
    fields = (
        'public_name',
        'contact_name',
        'organization_name',
        'description',
    )


@register(Corporation)
class CorporationTranslationOptions(TranslationOptions):
    fields = (
        'public_name',
        'organization_name',
        'description',
    )


@register(Specialist)
class SpecialistTranslationOptions(TranslationOptions):
    fields = (
        'experience',
    )
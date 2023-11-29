import django_filters
from .models import (
   StartUp,
   Investor,
   InvestFund,
   Corporation,
   Specialist,
)
from modules.models import (
    StartUpStage, 
    Industry, 
    BussinessModel, 
    Technology, 
    SellingModel, 
    Country, 
    InnovationMethod, 
    InvestStage
)


class StartUpFilter(django_filters.FilterSet):
    industries = django_filters.ModelMultipleChoiceFilter(
        field_name = 'industries',
        to_field_name = 'id',
        queryset = Industry.objects.all(),
    )
    technologies = django_filters.ModelMultipleChoiceFilter(
        field_name = 'technologies',
        to_field_name = 'id',
        queryset = Technology.objects.all(),
    )
    startup_stage = django_filters.ModelMultipleChoiceFilter(
        field_name = 'startup_stage',
        to_field_name = 'id',
        queryset = StartUpStage.objects.all(),
    )
    invest_stage = django_filters.ModelMultipleChoiceFilter(
        field_name = 'invest_stage',
        to_field_name = 'id',
        queryset = InvestStage.objects.all(),
    )
    selling_models = django_filters.ModelMultipleChoiceFilter(
        field_name = 'selling_models',
        to_field_name = 'id',
        queryset = SellingModel.objects.all(),
    )
    
    class Meta:
        model = StartUp
        fields = (
            'industries',
            'technologies',
            'startup_stage',
            'invest_stage',
            'selling_models',
            'employees_count',
            'organization_year'
        )


class InvestorFilter(django_filters.FilterSet):
    industries = django_filters.ModelMultipleChoiceFilter(
        field_name = 'industries',
        to_field_name = 'id',
        queryset = Industry.objects.all(),
    )
    technologies = django_filters.ModelMultipleChoiceFilter(
        field_name = 'technologies',
        to_field_name = 'id',
        queryset = Technology.objects.all(),
    )
    invest_rounds = django_filters.ModelMultipleChoiceFilter(
        field_name = 'invest_rounds',
        to_field_name = 'id',
        queryset = InvestStage.objects.all(),
    )
    class Meta:
        model = Investor
        fields = (
            'industries',
            'technologies',
            'invest_rounds'
        )


class InvestFundFilter(django_filters.FilterSet):
    industries = django_filters.ModelMultipleChoiceFilter(
        field_name = 'industries',
        to_field_name = 'id',
        queryset = Industry.objects.all(),
    )
    technologies = django_filters.ModelMultipleChoiceFilter(
        field_name = 'technologies',
        to_field_name = 'id',
        queryset = Technology.objects.all(),
    )
    invest_rounds = django_filters.ModelMultipleChoiceFilter(
        field_name = 'invest_rounds',
        to_field_name = 'id',
        queryset = InvestStage.objects.all(),
    )
    class Meta:
        model = InvestFund
        fields = (
            'industries',
            'technologies',
            'invest_rounds'
        )


class CorporationFilter(django_filters.FilterSet):
    industries = django_filters.ModelMultipleChoiceFilter(
        field_name = 'industries',
        to_field_name = 'id',
        queryset = Industry.objects.all(),
    )
    technologies = django_filters.ModelMultipleChoiceFilter(
        field_name = 'technologies',
        to_field_name = 'id',
        queryset = Technology.objects.all(),
    )

    class Meta:
        model = Corporation
        fields = (
            'industries',
            'technologies',
        )


class SpecialistFilter(django_filters.FilterSet):
    industries = django_filters.ModelMultipleChoiceFilter(
        field_name = 'industries',
        to_field_name = 'id',
        queryset = Industry.objects.all(),
    )
    technologies = django_filters.ModelMultipleChoiceFilter(
        field_name = 'technologies',
        to_field_name = 'id',
        queryset = Technology.objects.all(),
    )

    class Meta:
        model = Specialist
        fields = (
            'industries',
            'technologies',
            'experience_years'
        )


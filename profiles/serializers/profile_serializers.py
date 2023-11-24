from rest_framework import serializers
from ..models import (
   PilotProject,
   StartUp,
   Investor,
   InvestFund,
   Corporation,
   Specialist,
)
from users.serializers import (
    AppUserSerializer,
)

class PilotProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = PilotProject
        fields = (
            'title',
            'description'
        )


class StartUpProfileCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StartUp
        exclude = (
            'is_approved',
            'views', 
            'created', 
            'updated'
        )

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        instance.is_approved = False
        instance.save()

        return instance


class StartUpProfileDetailSerializer(serializers.ModelSerializer):
    technologies = serializers.ListField()
    industries = serializers.ListField()
    selling_models = serializers.ListField()
    startup_stage = serializers.CharField(
        source = 'startup_stage.name',
    )
    class Meta:
        model = StartUp
        fields = (
            'id',
            'is_approved',
            'startup_name',
            'website',
            'contact_name',
            'email',
            'phone',
            'organization_name',
            'organization_id',
            'organization_year',
            'employees_count',
            'description',
            'startup_stage',
            'invest_stage',
            'industries',
            'technologies',
            'bussiness_models',
            'selling_models',
            'countries',
            'have_sellings',
            'have_pilots',
            'active_search',
            'invested_sum',
            'investors',
            'logo',
            'presentation',
            'views',
            'created', 
            'updated'
        )


class InvestorProfileCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investor
        exclude = (
            'is_approved',
            'views', 
            'created', 
            'updated'
        )

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        instance.is_approved = False
        instance.save()

        return instance


class InvestorProfileDetailSerializer(serializers.ModelSerializer):
    technologies = serializers.ListField()
    industries = serializers.ListField()
    methods = serializers.ListField()
    stage = serializers.ListField()
    country = serializers.CharField(
        source = 'country.name',
    )
    class Meta:
        model = Investor
        fields = (
            'id',
            'is_approved',
            'profile_image',
            'contact_name',
            'email',
            'phone',
            'country',
            'description',
            'invest_sum',
            'methods',
            'stage',
            'technologies',
            'industries',
            'views',
            'created', 
            'updated'
        )


class InvestFundProfileCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestFund
        exclude = (
            'is_approved',
            'views', 
            'created', 
            'updated'
        )

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        instance.is_approved = False
        instance.save()

        return instance


class InvestFundProfileDetailSerializer(serializers.ModelSerializer):
    technologies = serializers.ListField()
    industries = serializers.ListField()
    methods = serializers.ListField()
    stage = serializers.ListField()
    country = serializers.CharField(
        source = 'country.name',
    )
    class Meta:
        model = InvestFund
        fields = (
            'id',
            'is_approved',
            'logo',
            'views',
            'public_name',
            'contact_name',
            'email',
            'phone',
            'organization_name',
            'organization_id',
            'country',
            'website',
            'description',
            'invest_sum',
            'methods',
            'stage',
            'technologies',
            'industries',
            'created', 
            'updated'
        )


class CorporationProfileCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corporation
        exclude = (
            'is_approved',
            'views', 
            'created', 
            'updated'
        )

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        instance.is_approved = False
        instance.save()

        return instance


class CorporationProfileDetailSerializer(serializers.ModelSerializer):
    technologies = serializers.ListField()
    industries = serializers.ListField()
    methods = serializers.ListField()
    stage = serializers.ListField()
    country = serializers.CharField(
        source = 'country.name',
    )
    class Meta:
        model = Corporation
        fields = (
            'id',
            'is_approved',
            'logo',
            'views',
            'public_name',
            'organization_name',
            'organization_id',
            'description',
            'country',
            'website',
            'email',
            'stage',
            'methods',
            'technologies',
            'industries',
            'created', 
            'updated'
        )


class SpecialistProfileCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialist
        exclude = (
            'is_approved',
            'views', 
            'created', 
            'updated'
        )

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        instance.is_approved = False
        instance.save()

        return instance


class SpecialistProfileDetailSerializer(serializers.ModelSerializer):
    technologies = serializers.ListField()
    industries = serializers.ListField()
    user = AppUserSerializer()
    class Meta:
        model = Specialist
        fields = (
            'id',
            'is_approved',
            'profile_image',
            'views',
            'user',
            'experience_years',
            'experience',
            'industries',
            'technologies',
            'resume',
            'created', 
            'updated'
        )
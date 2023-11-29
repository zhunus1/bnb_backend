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
    technologies = serializers.SerializerMethodField()
    industries = serializers.SerializerMethodField()
    selling_models = serializers.SerializerMethodField()
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
    
    def get_technologies(self, obj):
        return [tech.name for tech in obj.technologies.all()]
    
    def get_industries(self, obj):
        return [industry.name for industry in obj.industries.all()]
    
    def get_selling_models(self, obj):
        return [model.name for model in obj.selling_models.all()]


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
    technologies = serializers.SerializerMethodField()
    industries = serializers.SerializerMethodField()
    methods = serializers.SerializerMethodField()
    stage = serializers.SerializerMethodField()
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

    def get_technologies(self, obj):
        return [tech.name for tech in obj.technologies.all()]
    
    def get_industries(self, obj):
        return [industry.name for industry in obj.industries.all()]
    
    def get_methods(self, obj):
        return [method.name for method in obj.methods.all()]

    def get_stage(self, obj):
        return [stage.name for stage in obj.stage.all()]


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
    technologies = serializers.SerializerMethodField()
    industries = serializers.SerializerMethodField()
    methods = serializers.SerializerMethodField()
    stage = serializers.SerializerMethodField()
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
    
    def get_technologies(self, obj):
        return [tech.name for tech in obj.technologies.all()]
    
    def get_industries(self, obj):
        return [industry.name for industry in obj.industries.all()]
    
    def get_methods(self, obj):
        return [method.name for method in obj.methods.all()]

    def get_stage(self, obj):
        return [stage.name for stage in obj.stage.all()]


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
    technologies = serializers.SerializerMethodField()
    industries = serializers.SerializerMethodField()
    methods = serializers.SerializerMethodField()
    stage = serializers.SerializerMethodField()
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
    
    def get_technologies(self, obj):
        return [tech.name for tech in obj.technologies.all()]
    
    def get_industries(self, obj):
        return [industry.name for industry in obj.industries.all()]
    
    def get_methods(self, obj):
        return [method.name for method in obj.methods.all()]

    def get_stage(self, obj):
        return [stage.name for stage in obj.stage.all()]


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
    technologies = serializers.SerializerMethodField()
    industries = serializers.SerializerMethodField()
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
    
    def get_technologies(self, obj):
        return [tech.name for tech in obj.technologies.all()]
    
    def get_industries(self, obj):
        return [industry.name for industry in obj.industries.all()]
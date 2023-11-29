from rest_framework import serializers
from ..models import (
   StartUp,
   Investor,
   InvestFund,
   Corporation,
   Specialist,
)


class StartUpListSerializer(serializers.ModelSerializer):
    technologies = serializers.SerializerMethodField()
    class Meta:
        model = StartUp
        fields = (
            'id', 
            'logo',
            'startup_name',
            'description',
            'technologies',
        )
        
    def get_technologies(self, obj):
        return [tech.name for tech in obj.technologies.all()]


class StartUpDetailSerializer(serializers.ModelSerializer):
    technologies = serializers.SerializerMethodField()
    industries = serializers.SerializerMethodField()
    startup_stage_name = serializers.CharField(
        source = 'startup_stage.name',
    )
    invest_stage_name = serializers.CharField(
        source = 'invest_stage.name',
    )
    selling_models = serializers.SerializerMethodField()
    class Meta:
        model = StartUp
        fields = (
            'id', 
            'logo',
            'description',
            'organization_year',
            'employees_count',
            'technologies',
            'industries',
            'startup_stage_name',
            'invest_stage_name',
            'selling_models',
            'website',
            'presentation'
        )
    
    def get_technologies(self, obj):
        return [tech.name for tech in obj.technologies.all()]
    
    def get_industries(self, obj):
        return [industry.name for industry in obj.industries.all()]
    
    def get_selling_models(self, obj):
        return [model.name for model in obj.selling_models.all()]


class StartUpCreateSerializer(serializers.ModelSerializer):
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


class InvestorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investor
        fields = (
            'id', 
            'contact_name',
            'description',
            'profile_image',
        )


class InvestorDetailSerializer(serializers.ModelSerializer):
    technologies = serializers.SerializerMethodField()
    industries = serializers.SerializerMethodField()
    class Meta:
        model = Investor
        fields = (
            'id', 
            'profile_image',
            'contact_name',
            'description',
            'technologies',
            'industries',
            'email',
        )

    def get_technologies(self, obj):
        return [tech.name for tech in obj.technologies.all()]
    
    def get_industries(self, obj):
        return [industry.name for industry in obj.industries.all()]
    

class InvestFundListSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestFund
        fields = (
            'id', 
            'logo',
            'public_name',
            'description',
        )


class InvestFundDetailSerializer(serializers.ModelSerializer):
    technologies = serializers.SerializerMethodField()
    industries = serializers.SerializerMethodField()
    class Meta:
        model = InvestFund
        fields = (
            'id', 
            'logo',
            'public_name',
            'description',
            'technologies',
            'industries',
            'email',
            'website'
        )
    
    def get_technologies(self, obj):
        return [tech.name for tech in obj.technologies.all()]
    
    def get_industries(self, obj):
        return [industry.name for industry in obj.industries.all()]


class CorporationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corporation
        fields = (
            'id', 
            'logo',
            'public_name',
            'description',
        )


class CorporationDetailSerializer(serializers.ModelSerializer):
    technologies = serializers.SerializerMethodField()
    industries = serializers.SerializerMethodField()
    class Meta:
        model = Corporation
        fields = (
            'id', 
            'logo',
            'public_name',
            'description',
            'technologies',
            'industries',
            'email',
            'website'
        )

    def get_technologies(self, obj):
        return [tech.name for tech in obj.technologies.all()]
    
    def get_industries(self, obj):
        return [industry.name for industry in obj.industries.all()]


class SpecialistListSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        source = 'user.name',
    )
    technologies = serializers.SerializerMethodField()
    industries = serializers.SerializerMethodField()
    class Meta:
        model = Specialist
        fields = (
            'id', 
            'name',
            'profile_image',
            'industries',
            'technologies'
        )

    def get_technologies(self, obj):
        return [tech.name for tech in obj.technologies.all()]
    
    def get_industries(self, obj):
        return [industry.name for industry in obj.industries.all()]
   

class SpecialistDetailSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        source = 'user.name',
    )
    technologies = serializers.SerializerMethodField()
    industries = serializers.SerializerMethodField()
    email = serializers.CharField(
        source = 'user.email',
    )
    class Meta:
        model = Specialist
        fields = (
            'id', 
            'name',
            'profile_image',
            'experience',
            'experience_years',
            'industries',
            'technologies',
            'email',
            'resume'
        )
    
    def get_technologies(self, obj):
        return [tech.name for tech in obj.technologies.all()]
    
    def get_industries(self, obj):
        return [industry.name for industry in obj.industries.all()]
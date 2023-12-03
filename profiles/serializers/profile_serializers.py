from rest_framework import serializers
from ..models import (
   PilotProject,
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

class StartUpProfileCreateSerializer(serializers.ModelSerializer):
    countries = serializers.PrimaryKeyRelatedField(
        queryset = Country.objects.all(), 
        many = True
    )
    selling_models = serializers.PrimaryKeyRelatedField(
        queryset = SellingModel.objects.all(), 
        many = True
    )
    bussiness_models = serializers.PrimaryKeyRelatedField(
        queryset=BussinessModel.objects.all(), 
        many = True
    )
    technologies = serializers.PrimaryKeyRelatedField(
        queryset = Technology.objects.all(), 
        many = True
    )
    industries = serializers.PrimaryKeyRelatedField(
        queryset = Industry.objects.all(), 
        many = True
    )

    class Meta:
        model = StartUp
        fields = (
            'startup_name',
            'website',
            'contact_name',
            'email',
            'phone',
            'organization_name',
            'organization_id',
            'organization_year',
            'country',
            'employees_count',
            'description',
            'startup_stage',
            'invest_stage',
            'technologies',
            'industries',
            'bussiness_models',
            'selling_models',
            'countries',
            'have_sellings',
            'have_pilots',
            'active_search',
            'invested_sum',
            'investors',
            'user',
            'logo',
            'presentation',
            'information_source'
        )
    
    def create(self, validated_data):

        countries_data = validated_data.pop('countries', [])
        selling_models_data = validated_data.pop('selling_models', [])
        technologies_data = validated_data.pop('technologies', [])
        industries_data = validated_data.pop('industries', [])
        bussiness_models_data = validated_data.pop('bussiness_models', [])

        startup = StartUp.objects.create(**validated_data)

        startup.countries.set(countries_data)
        startup.selling_models.set(selling_models_data)
        startup.bussiness_models.set(bussiness_models_data)
        startup.technologies.set(technologies_data)
        startup.industries.set(industries_data)

        return startup


class StartUpProfileUpdateSerializer(serializers.ModelSerializer):
    selling_models = serializers.PrimaryKeyRelatedField(
        queryset = SellingModel.objects.all(), 
        many = True
    )
    bussiness_models = serializers.PrimaryKeyRelatedField(
        queryset=BussinessModel.objects.all(), 
        many = True
    )
    technologies = serializers.PrimaryKeyRelatedField(
        queryset = Technology.objects.all(), 
        many = True
    )
    industries = serializers.PrimaryKeyRelatedField(
        queryset = Industry.objects.all(), 
        many = True
    )
    

    class Meta:
        model = StartUp
        fields = (
            'startup_name',
            'description',
            'startup_stage',
            'bussiness_models',
            'technologies',
            'industries',
            'website',
            'logo',
            'presentation',
            'organization_name',
            'organization_id',
            'organization_year',
            'country',
            'selling_models',
            'employees_count',
            'contact_name',
            'email',
            'phone',
        )
    
    def update(self, instance, validated_data):
        instance.startup_name = validated_data.get('startup_name', instance.startup_name)
        instance.description = validated_data.get('description', instance.description)
        instance.startup_stage = validated_data.get('startup_stage', instance.startup_stage)
        instance.website = validated_data.get('website', instance.website)
        instance.logo = validated_data.get('logo', instance.logo)
        instance.presentation = validated_data.get('presentation', instance.presentation)
        instance.organization_name = validated_data.get('organization_name', instance.organization_name)
        instance.organization_id = validated_data.get('organization_id', instance.organization_id)
        instance.organization_year = validated_data.get('organization_year', instance.organization_year)
        instance.country = validated_data.get('country', instance.country)
        instance.employees_count = validated_data.get('employees_count', instance.employees_count)
        instance.contact_name = validated_data.get('contact_name', instance.contact_name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)

        instance.selling_models.set(validated_data.get('selling_models', instance.selling_models.all()))
        instance.bussiness_models.set(validated_data.get('bussiness_models', instance.bussiness_models.all()))
        instance.technologies.set(validated_data.get('technologies', instance.technologies.all()))
        instance.industries.set(validated_data.get('industries', instance.industries.all()))
        instance.is_approved = False
        instance.save()

        return instance
    
    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True  # Allow partial updates
        super().__init__(*args, **kwargs)


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


class InvestorProfileCreateSerializer(serializers.ModelSerializer):
    methods = serializers.PrimaryKeyRelatedField(
        queryset = InnovationMethod.objects.all(), 
        many = True
    )
    stage = serializers.PrimaryKeyRelatedField(
        queryset=StartUpStage.objects.all(), 
        many = True
    )
    technologies = serializers.PrimaryKeyRelatedField(
        queryset = Technology.objects.all(), 
        many = True
    )
    industries = serializers.PrimaryKeyRelatedField(
        queryset = Industry.objects.all(), 
        many = True
    )
    invest_rounds = serializers.PrimaryKeyRelatedField(
        queryset = InvestStage.objects.all(), 
        many = True
    )
    geography = serializers.PrimaryKeyRelatedField(
        queryset = Country.objects.all(), 
        many = True
    )
    pilotprojects = PilotProjectSerializer(
        many = True, 
        required = False,
    )

    class Meta:
        model = Investor
        fields = (
            'contact_name',
            'email',
            'phone',
            'country',
            'description',
            'profile_image',
            'information_source',
            'invest_sum',
            'methods',
            'stage',
            'technologies',
            'industries',
            'have_experience',
            'is_investing',
            'invest_rounds',
            'geography',
            'user',
            'pilotprojects'
        )
    
    def create(self, validated_data):
        pilots = validated_data.pop('pilotprojects', [])

        methods_data = validated_data.pop('methods', [])
        stage_data = validated_data.pop('stage', [])
        technologies_data = validated_data.pop('technologies', [])
        industries_data = validated_data.pop('industries', [])
        invest_rounds_data = validated_data.pop('invest_rounds', [])
        geography_data = validated_data.pop('geography', [])

        investor = Investor.objects.create(**validated_data)

        investor.methods.set(methods_data)
        investor.stage.set(stage_data)
        investor.technologies.set(technologies_data)
        investor.industries.set(industries_data)
        investor.invest_rounds.set(invest_rounds_data)
        investor.geography.set(geography_data)

        for pilot in pilots:
            pilot['content_object'] = investor
            PilotProject.objects.create(**pilot)
        return investor


class InvestorProfileUpdateSerializer(serializers.ModelSerializer):
    methods = serializers.PrimaryKeyRelatedField(
        queryset = InnovationMethod.objects.all(), 
        many = True
    )
    stage = serializers.PrimaryKeyRelatedField(
        queryset=StartUpStage.objects.all(), 
        many = True
    )
    technologies = serializers.PrimaryKeyRelatedField(
        queryset = Technology.objects.all(), 
        many = True
    )
    industries = serializers.PrimaryKeyRelatedField(
        queryset = Industry.objects.all(), 
        many = True
    )
    invest_rounds = serializers.PrimaryKeyRelatedField(
        queryset = InvestStage.objects.all(), 
        many = True
    )
    geography = serializers.PrimaryKeyRelatedField(
        queryset = Country.objects.all(), 
        many = True
    )
    

    class Meta:
        model = Investor
        fields = (
            'contact_name',
            'email',
            'phone',
            'country',
            'description',
            'profile_image',
            'invest_sum',
            'methods',
            'stage',
            'technologies',
            'industries',
            'invest_rounds',
            'geography',
        )
    
    def update(self, instance, validated_data):
        instance.contact_name = validated_data.get('contact_name', instance.contact_name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.country = validated_data.get('country', instance.country)
        instance.description = validated_data.get('description', instance.description)
        instance.invest_sum = validated_data.get('invest_sum', instance.invest_sum)
        instance.profile_image = validated_data.get('profile_image', instance.profile_image)

        instance.methods.set(validated_data.get('methods', instance.methods.all()))
        instance.stage.set(validated_data.get('stage', instance.stage.all()))
        instance.technologies.set(validated_data.get('technologies', instance.technologies.all()))
        instance.industries.set(validated_data.get('industries', instance.industries.all()))
        instance.invest_rounds.set(validated_data.get('invest_rounds', instance.invest_rounds.all()))
        instance.geography.set(validated_data.get('geography', instance.geography.all()))
        instance.is_approved = False
        instance.save()

        return instance
    
    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True  # Allow partial updates
        super().__init__(*args, **kwargs)


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


class InvestFundProfileCreateSerializer(serializers.ModelSerializer):
    methods = serializers.PrimaryKeyRelatedField(
        queryset = InnovationMethod.objects.all(), 
        many = True
    )
    stage = serializers.PrimaryKeyRelatedField(
        queryset=StartUpStage.objects.all(), 
        many = True
    )
    technologies = serializers.PrimaryKeyRelatedField(
        queryset = Technology.objects.all(), 
        many = True
    )
    industries = serializers.PrimaryKeyRelatedField(
        queryset = Industry.objects.all(), 
        many = True
    )
    invest_rounds = serializers.PrimaryKeyRelatedField(
        queryset = InvestStage.objects.all(), 
        many = True
    )
    geography = serializers.PrimaryKeyRelatedField(
        queryset = Country.objects.all(), 
        many = True
    )
    pilotprojects = PilotProjectSerializer(
        many = True, 
        required = False,
    )

    class Meta:
        model = InvestFund
        fields = (
            'public_name',
            'contact_name',
            'email',
            'phone',
            'organization_name',
            'organization_id',
            'country',
            'website',
            'description',
            'logo',
            'information_source',
            'invest_sum',
            'methods',
            'stage',
            'technologies',
            'industries',
            'have_experience',
            'is_investing',
            'invest_rounds',
            'geography',
            'user',
            'pilotprojects'
        )
    
    def create(self, validated_data):
        pilots = validated_data.pop('pilotprojects', [])

        methods_data = validated_data.pop('methods', [])
        stage_data = validated_data.pop('stage', [])
        technologies_data = validated_data.pop('technologies', [])
        industries_data = validated_data.pop('industries', [])
        invest_rounds_data = validated_data.pop('invest_rounds', [])
        geography_data = validated_data.pop('geography', [])

        investfund = InvestFund.objects.create(**validated_data)

        investfund.methods.set(methods_data)
        investfund.stage.set(stage_data)
        investfund.technologies.set(technologies_data)
        investfund.industries.set(industries_data)
        investfund.invest_rounds.set(invest_rounds_data)
        investfund.geography.set(geography_data)

        for pilot in pilots:
            pilot['content_object'] = investfund
            PilotProject.objects.create(**pilot)
        return investfund


class InvestFundProfileUpdateSerializer(serializers.ModelSerializer):
    methods = serializers.PrimaryKeyRelatedField(
        queryset = InnovationMethod.objects.all(), 
        many = True
    )
    stage = serializers.PrimaryKeyRelatedField(
        queryset=StartUpStage.objects.all(), 
        many = True
    )
    technologies = serializers.PrimaryKeyRelatedField(
        queryset = Technology.objects.all(), 
        many = True
    )
    industries = serializers.PrimaryKeyRelatedField(
        queryset = Industry.objects.all(), 
        many = True
    )
    

    class Meta:
        model = InvestFund
        fields = (
            'public_name',
            'logo',
            'contact_name',
            'phone',
            'email',
            'organization_name',
            'organization_id',
            'country',
            'description',
            'website',
            'invest_sum',
            'stage',
            'technologies',
            'industries',
            'methods'
        )
    
    def update(self, instance, validated_data):
        instance.public_name = validated_data.get('public_name', instance.public_name)
        instance.logo = validated_data.get('logo', instance.logo)
        instance.contact_name = validated_data.get('contact_name', instance.contact_name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.email = validated_data.get('email', instance.email)
        instance.organization_name = validated_data.get('organization_name', instance.organization_name)
        instance.organization_id = validated_data.get('organization_id', instance.organization_id)
        instance.country = validated_data.get('country', instance.country)
        instance.description = validated_data.get('description', instance.description)
        instance.website = validated_data.get('website', instance.website)
        instance.invest_sum = validated_data.get('invest_sum', instance.invest_sum)

        instance.methods.set(validated_data.get('methods', instance.methods.all()))
        instance.stage.set(validated_data.get('stage', instance.stage.all()))
        instance.technologies.set(validated_data.get('technologies', instance.technologies.all()))
        instance.industries.set(validated_data.get('industries', instance.industries.all()))
        instance.is_approved = False
        instance.save()

        return instance
    
    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True  # Allow partial updates
        super().__init__(*args, **kwargs)


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


class CorporationProfileCreateSerializer(serializers.ModelSerializer):
    methods = serializers.PrimaryKeyRelatedField(
        queryset = InnovationMethod.objects.all(), 
        many = True
    )
    stage = serializers.PrimaryKeyRelatedField(
        queryset=StartUpStage.objects.all(), 
        many = True
    )
    technologies = serializers.PrimaryKeyRelatedField(
        queryset = Technology.objects.all(), 
        many = True
    )
    industries = serializers.PrimaryKeyRelatedField(
        queryset = Industry.objects.all(), 
        many = True
    )
    invest_rounds = serializers.PrimaryKeyRelatedField(
        queryset = InvestStage.objects.all(), 
        many = True
    )
    geography = serializers.PrimaryKeyRelatedField(
        queryset = Country.objects.all(), 
        many = True
    )
    pilotprojects = PilotProjectSerializer(
        many = True, 
        required = False,
    )

    class Meta:
        model = Corporation
        fields = (
            'public_name',
            'email',
            'organization_name',
            'organization_id',
            'country',
            'website',
            'description',
            'logo',
            'information_source',
            'methods',
            'stage',
            'technologies',
            'industries',
            'have_experience',
            'is_investing',
            'invest_rounds',
            'geography',
            'user',
            'pilotprojects'
        )
    
    def create(self, validated_data):
        pilots = validated_data.pop('pilotprojects', [])

        methods_data = validated_data.pop('methods', [])
        stage_data = validated_data.pop('stage', [])
        technologies_data = validated_data.pop('technologies', [])
        industries_data = validated_data.pop('industries', [])
        invest_rounds_data = validated_data.pop('invest_rounds', [])
        geography_data = validated_data.pop('geography', [])

        corporation = Corporation.objects.create(**validated_data)

        corporation.methods.set(methods_data)
        corporation.stage.set(stage_data)
        corporation.technologies.set(technologies_data)
        corporation.industries.set(industries_data)
        corporation.invest_rounds.set(invest_rounds_data)
        corporation.geography.set(geography_data)

        for pilot in pilots:
            pilot['content_object'] = corporation
            PilotProject.objects.create(**pilot)
        return corporation


class CorporationProfileUpdateSerializer(serializers.ModelSerializer):
    methods = serializers.PrimaryKeyRelatedField(
        queryset = InnovationMethod.objects.all(), 
        many = True
    )
    stage = serializers.PrimaryKeyRelatedField(
        queryset=StartUpStage.objects.all(), 
        many = True
    )
    technologies = serializers.PrimaryKeyRelatedField(
        queryset = Technology.objects.all(), 
        many = True
    )
    industries = serializers.PrimaryKeyRelatedField(
        queryset = Industry.objects.all(), 
        many = True
    )
    pilotprojects = PilotProjectSerializer(
        many = True,
        required = False,
    )

    class Meta:
        model = Corporation
        fields = (
            'public_name',
            'logo',
            'organization_name',
            'organization_id',
            'description',
            'country',
            'website',
            'email',
            'stage',
            'technologies',
            'industries',
            'methods',
            'pilotprojects'
        )
    
    def update(self, instance, validated_data):
        instance.public_name = validated_data.get('public_name', instance.public_name)
        instance.logo = validated_data.get('logo', instance.logo)
        instance.organization_name = validated_data.get('organization_name', instance.organization_name)
        instance.organization_id = validated_data.get('organization_id', instance.organization_id)
        instance.country = validated_data.get('country', instance.country)
        instance.description = validated_data.get('description', instance.description)
        instance.email = validated_data.get('email', instance.email)
        instance.website = validated_data.get('website', instance.website)

        instance.methods.set(validated_data.get('methods', instance.methods.all()))
        instance.stage.set(validated_data.get('stage', instance.stage.all()))
        instance.technologies.set(validated_data.get('technologies', instance.technologies.all()))
        instance.industries.set(validated_data.get('industries', instance.industries.all()))
        instance.is_approved = False
        instance.save()

        pilotprojects_data = validated_data.pop('pilotprojects', [])
        for pilot_data in pilotprojects_data:
            pilot_data['content_type'] = instance.get_content_type()
            pilot_data['object_id'] = instance.id
            pilot_project_id = pilot_data.pop('id', None)

            if pilot_project_id:
                # If PilotProject ID is provided, update existing instance
                pilot_project = PilotProject.objects.get(id=pilot_project_id)
                for key, value in pilot_data.items():
                    setattr(pilot_project, key, value)
                pilot_project.save()
            else:
                # If no PilotProject ID is provided, create a new instance
                PilotProject.objects.create(**pilot_data)

        return instance
    
    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True  # Allow partial updates
        super().__init__(*args, **kwargs)


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


class SpecialistProfileCreateSerializer(serializers.ModelSerializer):
    technologies = serializers.PrimaryKeyRelatedField(
        queryset = Technology.objects.all(), 
        many = True
    )
    industries = serializers.PrimaryKeyRelatedField(
        queryset = Industry.objects.all(), 
        many = True
    )

    class Meta:
        model = Specialist
        fields = (
            'experience',
            'technologies',
            'industries',
            'experience_years',
            'profile_image',
            'resume',
            'information_source',
        )
    
    def create(self, validated_data):

        technologies_data = validated_data.pop('technologies', [])
        industries_data = validated_data.pop('industries', [])
        
        specialist = Specialist.objects.create(**validated_data)

        specialist.technologies.set(technologies_data)
        specialist.industries.set(industries_data)
        
        return specialist


class SpecialistProfileUpdateSerializer(serializers.ModelSerializer):
    technologies = serializers.PrimaryKeyRelatedField(
        queryset = Technology.objects.all(), 
        many = True
    )
    industries = serializers.PrimaryKeyRelatedField(
        queryset = Industry.objects.all(), 
        many = True
    )

    class Meta:
        model = Specialist
        fields = (
            'profile_image',
            'experience_years',
            'experience',
            'technologies',
            'industries',
            'resume'
        )
    
    def update(self, instance, validated_data):
        instance.profile_image = validated_data.get('profile_image', instance.profile_image)
        instance.experience_years = validated_data.get('experience_years', instance.experience_years)
        instance.experience = validated_data.get('experience', instance.experience)
        instance.resume = validated_data.get('resume', instance.resume)
       
        instance.technologies.set(validated_data.get('technologies', instance.technologies.all()))
        instance.industries.set(validated_data.get('industries', instance.industries.all()))
        instance.is_approved = False
        instance.save()

        return instance
    
    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True  # Allow partial updates
        super().__init__(*args, **kwargs)


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
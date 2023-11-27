from rest_framework import serializers
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


class InvestStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestStage
        fields = (
            'id', 
            'name',
        )


class StartUpStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StartUpStage
        fields = (
            'id', 
            'name',
        )


class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = (
            'id', 
            'name',
        )


class BussinessModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BussinessModel
        fields = (
            'id', 
            'name',
        )


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = (
            'id', 
            'name',
        )


class SellingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellingModel
        fields = (
            'id', 
            'name',
        )


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = (
            'id', 
            'name',
        )


class InnovationMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = InnovationMethod
        fields = (
            'id', 
            'name',
        )
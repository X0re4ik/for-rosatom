from .models import (
    Questionnaire, 
    Company, 
    Division)

from rest_framework import serializers
from django.db.models import Q


class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = ['name',]

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'division',]

class QuestionnaireSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    
    class Meta:
        model = Questionnaire
        fields = ['question', 'email', 'time_of_creat', 'company',]
    
    
    def create(self, validated_data: dict):
        tracks_data: dict = validated_data.pop('company')
        name, division = tracks_data.get('name'), tracks_data.get('division')
        company = Company.objects.filter(
            Q(name=name) &
            Q(division=division)
        ).first()
        if not company:
            company = Company.objects.create(
                name=name,
                division=division)
            company.save()
        questionnaire = Questionnaire.objects.create(
            company=company,
            **validated_data
        )
        return questionnaire





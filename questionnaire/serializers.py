from .models import (
    Questionnaire, 
    Company, 
    Division)

from rest_framework import serializers
from django.db.models import Q


class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class QuestionnaireSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    class Meta:
        model = Questionnaire
        fields = '__all__'


class AddQuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = '__all__'




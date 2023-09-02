from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.mixins import ListModelMixin


from .models import Division, Company
from .serializers import QuestionnaireSerializer, DivisionSerializer, CompanySerializer


class DivisionList(ListAPIView):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer

class CompaniesFromList(ListAPIView):
    def list(self, request, division_id: int):
        companies_from_division = Company.objects.filter(division=Division.objects.get(pk=division_id)).all()
        serializer = CompanySerializer(companies_from_division, many=True)
        return Response(serializer.data)

class AddQuestionnaire(CreateAPIView):
    serializer_class = QuestionnaireSerializer
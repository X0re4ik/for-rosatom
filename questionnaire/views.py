from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.mixins import ListModelMixin


from .models import Division, Company, Questionnaire
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
    
class QuestionsList(ListAPIView):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer
    
from django.db.models import Count

class GGG(APIView):
    
    def get(self, request):
        
        total_number_of_questionnaires = Questionnaire \
                                        .objects \
                                        .values('company') \
                                        .annotate(total=Count('id'))
        
        answer = [
            {
                "division": division.name,
                "company_and_total": []
            } for division in Division.objects.all()
        ]
        
        def __find_dict_with_division(division_name: str) -> int:
            for i, dict_ in enumerate(answer):
                if dict_["division"] == division_name:
                    return i
            return -1
    
        for value_ in total_number_of_questionnaires:
            company, total = value_['company'], value_['total']

            company_ = Company.objects.get(pk=company)
            division_ = company_.division
            index = __find_dict_with_division(division_.name)
            answer[index]["company_and_total"].append(
                {
                    "company": company_.name,
                    "total": total
                }
            )
        
        return Response(data=answer, status=status.HTTP_200_OK, headers={
            'Content-Type': 'application/json'
        })
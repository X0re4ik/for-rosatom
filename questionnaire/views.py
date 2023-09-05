from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader

from .models import Division, Company, Questionnaire
from .serializers import QuestionnaireSerializer, DivisionSerializer, CompanySerializer, AddQuestionnaireSerializer
from .forms import QuestionnaireForm

class DivisionList(ListAPIView):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer

class CompaniesFromList(ListAPIView):
    def list(self, request, division_id: int):
        companies_from_division = Company.objects.filter(division=Division.objects.get(pk=division_id)).all()
        serializer = CompanySerializer(companies_from_division, many=True)
        return Response(serializer.data)

class AddCompany(CreateAPIView):
    serializer_class = CompanySerializer

class AddQuestionnaire(CreateAPIView):
    serializer_class = AddQuestionnaireSerializer
    
class QuestionsList(ListAPIView):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer

class Statistics(APIView):
    
    def get(self, request):
        companies = Company.objects.all()
        answer = []
        for company in companies:
            answer.append({
                "company": company.name,
                "division": company.division.name,
                "total": company.number_of_questions
            })
        return Response(data=answer, status=status.HTTP_200_OK)
        

def question_statistics(request):
    template = loader.get_template("statistics.html")
    
    context = {
        "questionnaires": QuestionsList.as_view()(request=request).data,
        "statistics": Statistics.as_view()(request=request).data
    }
    
    return HttpResponse(template.render(context, request))


def directors_day_questionnaire(request):
    template = loader.get_template("questionnaire.html")
    if request.method == 'POST':
        new_company = request.POST.get("new_company")
        
        company = None
        if new_company:
            division_id = request.POST.get("division")
            company, created = Company.objects.get_or_create(
                name=new_company,
                division=Division.objects.get(pk=division_id)
            )
              
        if not company:
            company_id = request.POST.get("company")
            company = Company.objects.get(pk=company_id)
        
        email = request.POST.get("email")
        question = request.POST.get("question")
        
        Questionnaire.objects.create(
            question=question,
            email=email if email else None,
            company=company
        )
    
    context = {
        "form": QuestionnaireForm()
    }
    
    return HttpResponse(template.render(context, request))
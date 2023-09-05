from django.urls import path, include

from .views import (
    DivisionList, 
    CompaniesFromList, 
    AddQuestionnaire, 
    QuestionsList,
    Statistics, AddCompany,
    directors_day_questionnaire,
    question_statistics)

API_VERSION = 1

urlpatterns_api = [
    path('list_of_divisions',   DivisionList.as_view()),
    path('add_of_company', AddCompany.as_view()),
    path('companies_from/<int:division_id>', CompaniesFromList.as_view()),
    path('add', AddQuestionnaire.as_view()),
    path('list', QuestionsList.as_view(), name='questions_list'),
    path('statistics', Statistics.as_view()),
]

urlpatterns = [
    path(f"api/v{API_VERSION}/", include(urlpatterns_api)),
    path('', directors_day_questionnaire),
    path('statistics', question_statistics, name='question_statistics'),
]
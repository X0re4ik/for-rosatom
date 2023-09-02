from django.urls import path

from .views import DivisionList, CompaniesFromList, AddQuestionnaire

urlpatterns = [
    path('list_of_divisions',   DivisionList.as_view()),
    path('companies_from/<int:division_id>',   CompaniesFromList.as_view()),
    path('add_questionnaire', AddQuestionnaire.as_view())
]
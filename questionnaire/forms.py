from django import forms

from .models import Questionnaire, Company, Division

class QuestionnaireForm(forms.ModelForm):
    class Meta:
        model = Questionnaire
        fields = ['email', 'question']
    
    division = forms.ChoiceField(
        label="Выберети дивизион",
        required=True,
        choices=[(0, "Выберете дивизион")] + [ (division.id, division.name) for division in Division.objects.all() ]
    )
    
    company = forms.ChoiceField(
        label="Выберети компанию",
        required=False,
    )
    
    new_company = forms.CharField(label="Не нашли свою компанию?", max_length=100, required=False)
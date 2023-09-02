from django.contrib import admin

from .models import Questionnaire, Company, Division
# Register your models here.

admin.site.register([Questionnaire, Company, Division])


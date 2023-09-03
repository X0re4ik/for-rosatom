from django.db import models

# Create your models here.

from datetime import datetime


class Division(models.Model):
    name = models.CharField(max_length=25, unique=True)
    
    def __str__(self) -> str:
        return f'Division: {self.name}'


class Company(models.Model):
    name = models.CharField(max_length=25)
    
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('name', 'division')
    
    def __str__(self) -> str:
        return f'Company {self.name}'


class Questionnaire(models.Model):
    question = models.TextField()
    email = models.EmailField(null=True, blank=True)
    time_of_creat = models.DateTimeField(default=datetime.now())
    
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'Questionnaire from {self.company} ({self.time_of_creat})'
# Generated by Django 3.2.20 on 2023-09-02 04:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0002_auto_20230902_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='time_of_creat',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 2, 9, 25, 50, 338842)),
        ),
    ]
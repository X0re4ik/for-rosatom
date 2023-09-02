# Generated by Django 3.2.20 on 2023-09-02 04:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='questionnaire.company'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='time_of_creat',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 2, 9, 15, 29, 954917)),
        ),
    ]

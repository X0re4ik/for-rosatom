# Generated by Django 3.2.20 on 2023-09-05 14:02

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('time_of_creat', models.DateTimeField(default=datetime.datetime(2023, 9, 5, 19, 2, 12, 829581))),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionnaire.company')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='division',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionnaire.division'),
        ),
        migrations.AlterUniqueTogether(
            name='company',
            unique_together={('name', 'division')},
        ),
    ]

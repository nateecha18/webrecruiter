# Generated by Django 2.0.6 on 2018-10-16 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapply', '0009_auto_20181016_0322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidatebasic',
            name='candidate_history_education',
        ),
        migrations.AddField(
            model_name='candidatebasic',
            name='candidate_history_education',
            field=models.ManyToManyField(to='jobapply.CandidateHistoryEducation'),
        ),
    ]

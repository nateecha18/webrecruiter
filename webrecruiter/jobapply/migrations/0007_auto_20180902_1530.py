# Generated by Django 2.0.6 on 2018-09-02 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobapply', '0006_auto_20180902_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidatebasic',
            name='candidate_attachment',
        ),
        migrations.AddField(
            model_name='candidateattachment',
            name='candidate_basic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jobapply.CandidateBasic'),
        ),
    ]

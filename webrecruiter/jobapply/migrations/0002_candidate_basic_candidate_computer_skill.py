# Generated by Django 2.0.6 on 2018-08-26 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobapply', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate_basic',
            name='candidate_computer_skill',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='jobapply.Candidate_Computer_Skill'),
        ),
    ]

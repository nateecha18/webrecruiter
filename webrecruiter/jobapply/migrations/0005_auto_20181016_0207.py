# Generated by Django 2.0.6 on 2018-10-16 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobapply', '0004_convertdatabase'),
    ]

    operations = [
        migrations.CreateModel(
            name='EducationLevel',
            fields=[
                ('value', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('education_level', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='ConvertDatabase',
        ),
        migrations.AddField(
            model_name='candidatebasic',
            name='nowEdu_level_new',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='jobapply.EducationLevel'),
        ),
    ]

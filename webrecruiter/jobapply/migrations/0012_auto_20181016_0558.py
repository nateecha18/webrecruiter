# Generated by Django 2.0.6 on 2018-10-16 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobapply', '0011_auto_20181016_0507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatehistoryeducation',
            name='edu_level',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='jobapply.EducationLevel'),
        ),
    ]

# Generated by Django 2.0.6 on 2018-10-16 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapply', '0010_auto_20181016_0430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatehistoryeducation',
            name='edu_level',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]

# Generated by Django 2.0.6 on 2018-10-29 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapply', '0027_auto_20181021_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatebasic',
            name='date_apply',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

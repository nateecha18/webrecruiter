# Generated by Django 2.0.6 on 2018-10-19 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapply', '0018_institute'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidatebasic',
            name='date_apply',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

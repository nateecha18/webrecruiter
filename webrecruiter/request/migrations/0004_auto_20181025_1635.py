# Generated by Django 2.0.6 on 2018-10-25 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0003_requestcandidate_vacancy_employee_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date_comment',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='requestcandidate',
            name='date_request',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

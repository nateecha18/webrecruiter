# Generated by Django 2.0.6 on 2018-11-16 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobapply', '0034_auto_20181116_2040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidatebasic',
            name='bdate',
        ),
    ]

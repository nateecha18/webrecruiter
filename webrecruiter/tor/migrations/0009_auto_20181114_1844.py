# Generated by Django 2.0.6 on 2018-11-14 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tor', '0008_auto_20181114_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='positionfield',
            name='certification',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='positionfield',
            name='note',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='positionfield',
            name='requirement',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
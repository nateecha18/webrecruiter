# Generated by Django 2.0.6 on 2018-10-11 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('rank', '0008_auto_20181011_0310'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidaterank',
            name='owner',
            field=models.ManyToManyField(to='account.Profile'),
        ),
    ]

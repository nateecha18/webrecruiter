# Generated by Django 2.0.6 on 2018-11-16 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapply', '0033_auto_20181116_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatebasic',
            name='bdate',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]

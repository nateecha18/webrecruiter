# Generated by Django 2.0.6 on 2018-11-16 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0024_auto_20181114_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_detail',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='requestcandidate',
            name='note',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='requestcandidate',
            name='requirement',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]

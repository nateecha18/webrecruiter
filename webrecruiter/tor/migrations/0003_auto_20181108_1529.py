# Generated by Django 2.0.6 on 2018-11-08 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tor', '0002_auto_20181108_1026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tor',
            name='job_field',
        ),
        migrations.RemoveField(
            model_name='tor',
            name='job_section',
        ),
        migrations.AddField(
            model_name='tor',
            name='position_edu_des',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='tor',
            name='position_exp_des',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='tor',
            name='position_role_des',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='tor',
            name='position_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]

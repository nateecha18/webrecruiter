# Generated by Django 2.0.6 on 2018-09-24 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(blank=True, max_length=50, null=True)),
                ('skill_type', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
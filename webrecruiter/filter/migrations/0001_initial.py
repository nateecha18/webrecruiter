# Generated by Django 2.0.6 on 2018-09-04 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FilterPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkbox_position', models.CharField(blank=True, max_length=50, null=True)),
                ('operator_position', models.CharField(blank=True, max_length=250, null=True)),
                ('filter_position', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]

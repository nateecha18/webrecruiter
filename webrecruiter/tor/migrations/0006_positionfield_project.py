# Generated by Django 2.0.6 on 2018-11-12 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0020_auto_20181106_0651'),
        ('account', '0001_initial'),
        ('tor', '0005_auto_20181110_1930'),
    ]

    operations = [
        migrations.CreateModel(
            name='PositionField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_type', models.CharField(blank=True, max_length=50, null=True)),
                ('position_tor_amount', models.IntegerField(blank=True, null=True)),
                ('position_now_amount', models.IntegerField(blank=True, null=True)),
                ('datetime_add_position', models.DateTimeField(auto_now_add=True)),
                ('datetime_update_position', models.DateTimeField(auto_now=True)),
                ('position_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Position_In_Project', to='request.Position')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(blank=True, max_length=100, null=True)),
                ('project_site', models.CharField(blank=True, max_length=100, null=True)),
                ('datetime_add_project', models.DateTimeField(auto_now_add=True)),
                ('datetime_update_project', models.DateTimeField(auto_now=True)),
                ('level', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tor.ProjectLevel')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Owner_Project', to='account.Profile')),
                ('positions', models.ManyToManyField(blank=True, to='tor.PositionField')),
                ('project_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tor.ProjectType')),
            ],
        ),
    ]

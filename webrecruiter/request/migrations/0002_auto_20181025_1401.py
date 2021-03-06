# Generated by Django 2.0.6 on 2018-10-25 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LevelRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_id', models.CharField(max_length=15)),
                ('level_name', models.CharField(max_length=100)),
                ('level_description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_type_id', models.CharField(max_length=15)),
                ('project_type_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='requestcandidate',
            name='comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='request_owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='request.RequestCandidate'),
        ),
        migrations.AddField(
            model_name='requestcandidate',
            name='certification',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='requestcandidate',
            name='note',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='requestcandidate',
            name='now_employee_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='requestcandidate',
            name='project_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='requestcandidate',
            name='project_site',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='requestcandidate',
            name='requirement',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='requestcandidate',
            name='tor_employee_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='requestcandidate',
            name='request_title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='requestcandidate',
            name='level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='request.LevelRequest'),
        ),
        migrations.AddField(
            model_name='requestcandidate',
            name='project_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='request.ProjectType'),
        ),
    ]

# Generated by Django 2.0.6 on 2018-11-05 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0019_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='request_position',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='request.Position'),
        ),
        migrations.AddField(
            model_name='request',
            name='request_position_other',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

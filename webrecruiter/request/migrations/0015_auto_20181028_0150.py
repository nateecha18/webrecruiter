# Generated by Django 2.0.6 on 2018-10-27 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0014_auto_20181028_0128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestcandidate',
            name='status',
        ),
        migrations.AddField(
            model_name='request',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='request.Status'),
        ),
    ]

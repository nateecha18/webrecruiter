# Generated by Django 2.0.6 on 2018-11-21 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0029_auto_20181121_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='updateamountlog',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='request.Comment'),
        ),
    ]

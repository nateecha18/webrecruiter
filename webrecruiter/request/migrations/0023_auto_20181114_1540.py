# Generated by Django 2.0.6 on 2018-11-14 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0022_auto_20181114_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='request_position',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tor.PositionAll'),
        ),
        migrations.DeleteModel(
            name='Position',
        ),
    ]

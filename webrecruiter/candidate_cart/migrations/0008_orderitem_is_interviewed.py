# Generated by Django 2.0.6 on 2018-11-06 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate_cart', '0007_auto_20181106_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='is_interviewed',
            field=models.BooleanField(default=False),
        ),
    ]

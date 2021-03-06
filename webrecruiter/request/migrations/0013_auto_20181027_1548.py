# Generated by Django 2.0.6 on 2018-10-27 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('request', '0012_auto_20181026_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestcandidate',
            name='last_comment_owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_updater', to='account.Profile'),
        ),
        migrations.AlterField(
            model_name='requestcandidate',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creator', to='account.Profile'),
        ),
    ]

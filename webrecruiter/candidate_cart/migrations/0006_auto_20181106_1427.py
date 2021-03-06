# Generated by Django 2.0.6 on 2018-11-06 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('candidate_cart', '0005_auto_20181028_0128'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Profile'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='candidate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='jobapply.CandidateBasic'),
        ),
    ]

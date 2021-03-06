# Generated by Django 2.0.6 on 2018-10-27 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('candidate_cart', '0005_auto_20181028_0128'),
        ('account', '0001_initial'),
        ('request', '0013_auto_20181027_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_id', models.CharField(max_length=15)),
                ('request_title', models.CharField(blank=True, max_length=200, null=True)),
                ('datetime_add_request', models.DateTimeField(auto_now_add=True)),
                ('datetime_update_request', models.DateTimeField(auto_now=True)),
                ('comment', models.ManyToManyField(to='request.Comment')),
                ('last_comment_owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_updater', to='account.Profile')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creator', to='account.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='RequestInterview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_interview', models.CharField(max_length=100)),
                ('note_interview', models.CharField(max_length=100)),
                ('order', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='candidate_cart.Order')),
            ],
        ),
        migrations.CreateModel(
            name='RequestType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_type_id', models.CharField(max_length=5)),
                ('request_type_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='requestcandidate',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='requestcandidate',
            name='datetime_add_request',
        ),
        migrations.RemoveField(
            model_name='requestcandidate',
            name='datetime_update_request',
        ),
        migrations.RemoveField(
            model_name='requestcandidate',
            name='last_comment_owner',
        ),
        migrations.RemoveField(
            model_name='requestcandidate',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='requestcandidate',
            name='request_id',
        ),
        migrations.RemoveField(
            model_name='requestcandidate',
            name='request_title',
        ),
        migrations.AddField(
            model_name='request',
            name='request_candidate',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='request.RequestCandidate'),
        ),
        migrations.AddField(
            model_name='request',
            name='request_interview',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='request.RequestInterview'),
        ),
        migrations.AddField(
            model_name='request',
            name='request_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='request.RequestType'),
        ),
    ]

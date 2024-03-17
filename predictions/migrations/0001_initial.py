# Generated by Django 4.1.13 on 2024-03-17 05:54

from django.db import migrations, models
import djongo.models.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CycleStatPrediction',
            fields=[
                ('cycle_stat_prediction_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user_id_hash', models.CharField(max_length=100)),
                ('average_cycle_length', djongo.models.fields.JSONField()),
                ('period_statistics', djongo.models.fields.JSONField()),
                ('next_period_prediction', djongo.models.fields.JSONField()),
                ('create_datetime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'cycle_stat_prediction',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PeriodPredictions',
            fields=[
                ('period_prediction_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user_id_hash', models.CharField(max_length=100)),
                ('user_data', djongo.models.fields.JSONField()),
                ('prediction_data', djongo.models.fields.JSONField()),
                ('create_datetime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'period_predictions',
                'managed': False,
            },
        ),
    ]
# Generated by Django 4.1.7 on 2024-05-04 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleEvents',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Subject', models.CharField(blank=True, max_length=200, null=True)),
                ('StartTime', models.DateTimeField()),
                ('EndTime', models.DateTimeField()),
                ('StartTimezone', models.CharField(blank=True, max_length=200, null=True)),
                ('EndTimezone', models.CharField(blank=True, max_length=200, null=True)),
                ('Location', models.CharField(blank=True, max_length=200, null=True)),
                ('Description', models.CharField(blank=True, max_length=200, null=True)),
                ('IsAllDay', models.BooleanField()),
                ('RecurrenceID', models.IntegerField(blank=True, null=True)),
                ('FollowingID', models.IntegerField(blank=True, null=True)),
                ('RecurrenceRule', models.CharField(blank=True, max_length=200, null=True)),
                ('RecurrenceException', models.CharField(blank=True, max_length=200, null=True)),
                ('IsReadonly', models.BooleanField(blank=True, null=True)),
                ('IsBlock', models.BooleanField(blank=True, null=True)),
                ('RoomID', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'schedule_events',
            },
        ),
    ]

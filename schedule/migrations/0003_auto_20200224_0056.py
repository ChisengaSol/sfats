# Generated by Django 3.0.3 on 2020-02-24 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_schedule_stafalty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='time',
            field=models.CharField(max_length=20),
        ),
    ]

# Generated by Django 3.0.3 on 2020-02-17 23:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200217_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='whoami',
            field=models.CharField(choices=[('STAFF', 'Staff'), ('FACULTY', 'Faculty')], default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avail_status',
            field=models.CharField(choices=[('AVAILBLE', 'Available'), ('UNAVAILABLE', 'Unavailable')], default='UNAVAILABLE', max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 3.0.3 on 2020-02-17 13:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('studentName', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=20, unique=True)),
                ('email_address', models.EmailField(max_length=254)),
                ('schedule_status', models.CharField(choices=[('ACCEPTED', 'Accepted'), ('DECLINED', 'Declined'), ('PENDING', 'Pending')], max_length=10)),
                ('stafalty', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

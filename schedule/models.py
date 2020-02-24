from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Schedule(models.Model):

    class Status(models.TextChoices):
        ACCEPTED = 'ACCEPTED'
        DECLINED = 'DECLINED'
        PENDING = 'PENDING'

    stafalty = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_scheduled')
    time = models.CharField(null=False, blank = False,max_length=20)
    studentName = models.TextField(max_length=255)
    phone_number = models.TextField(null=False, blank = False, unique=True, max_length=20)
    email_address = models. EmailField(max_length=254)
    schedule_status = models.CharField(null=False, blank = False,max_length=9, choices=Status.choices)

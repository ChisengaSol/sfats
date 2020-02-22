from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

class User(AbstractUser):
    username = models.TextField(max_length=50, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)

        
class UserProfile(models.Model):
    
    class WhoAmI(models.TextChoices):
        STAFF = 'STAFF'
        FACULTY = 'FACULTY'

    class AvailStatus (models.TextChoices):
        AVAILABLE= 'AVAILABLE'
        UNAVAILABLE = 'UNAVAILABLE'

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    title = models.CharField(max_length=5)
    address = models.TextField(max_length=255)
    phone_number = models.TextField(null=False, blank = False, unique=True, max_length=20)
    avail_status = models.TextField(max_length=20, null=False, blank = False, choices=AvailStatus.choices, default='UNAVAILABLE')
    whoami = models.TextField(null=False, blank = False,max_length=10, choices=WhoAmI.choices)
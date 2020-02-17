from rest_framework import serializers
from .models import Schedule
from users.serializer import UserSerializer

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

    stafalty = UserSerializer()
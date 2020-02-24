from rest_framework import serializers
from .models import Schedule
from users.serializer import UserSerializer

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

    user_details = UserSerializer(source='stafalty', read_only=True)
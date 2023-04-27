from .models import LeaveRequest
from rest_framework import serializers

class LeaveRequestCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveRequest
        fields = ['from_date', 'to_date', 'from_hour', 'to_hour', 'details']

class LeaveRequestUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveRequest
        fields = ["status"]
        read_only_fields = ['user', 'from-date', 'to_date', 'from_hour', 'to_hour', 'details']
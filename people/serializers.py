from rest_framework import serializers
from .models import Person
from users.serializers import UserListSerializer, SignUpSerializer
from users.models import CustomUser
from companies.models import ConfirmationCode, Role
from django.shortcuts import get_object_or_404

class EmployeeCreateSerializer(serializers.Serializer):
    user = SignUpSerializer()
    gender = serializers.ChoiceField(choices=Person.GENDER_FIELD, allow_null=True)
    phone_no = serializers.CharField(max_length=11)
    job_title = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all())
    confirmation_code = serializers.IntegerField()

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        job_title = validated_data.pop('job_title')
        confirmation_code_value = validated_data.pop('confirmation_code')
        confirmation_code = get_object_or_404(ConfirmationCode, value=confirmation_code_value)
        confirmation_code.is_used = True
        user = CustomUser.objects.create(**user_data)
        person = Person.objects.create(user=user, company=confirmation_code.company, job_title=job_title, **validated_data)
        confirmation_code.user = person
        confirmation_code.save()
        return {'user':user, 'job_title':job_title, 'confirmation_code':confirmation_code_value, 'gender':validated_data['gender'], 'phone_no':validated_data['phone_no']}


class EmployeeListSerializer(serializers.ModelSerializer):
    #user = serializers.CharField(source='user.username')
    user = UserListSerializer()
    class Meta:
        model = Person
        fields = "__all__"

class EmployeeUpdateSerializer(serializers.ModelSerializer):
    user = UserListSerializer()
    class Meta:
        model = Person
        exclude = ['company', 'is_employer', 'balance']
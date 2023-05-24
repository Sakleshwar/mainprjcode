from rest_framework import serializers
from .models import Employee, PayStub, TimeOffRequest

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class PayStubSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayStub
        fields = '__all__'

class TimeOffRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeOffRequest
        fields = '__all__'

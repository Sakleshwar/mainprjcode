from django import forms
from .models import Employee, PayStub, TimeOffRequest

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class PayStubForm(forms.ModelForm):
    class Meta:
        model = PayStub
        fields = '__all__'

class TimeOffRequestForm(forms.ModelForm):
    class Meta:
        model = TimeOffRequest
        fields = '__all__'



from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import EmployeeForm, PayStubForm, TimeOffRequestForm
from .serializers import EmployeeSerializer, PayStubSerializer, TimeOffRequestSerializer
from django.http import JsonResponse
from django.shortcuts import render

class EmployeeUpdateAPIView(APIView):
    def post(self, request):
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'Employee updated successfully'})
        else:
            return JsonResponse({'status': 'error', 'message': form.errors}, status=400)

class PayStubCreateAPIView(APIView):
    def post(self, request):
        form = PayStubForm(request.POST)
        if form.is_valid():
            pay_stub = form.save(commit=False)
            pay_stub.employee_id = 1  # Assuming 1 is the employee ID
            pay_stub.save()
            return JsonResponse({'status': 'success', 'message': 'Pay stub created successfully'})
        else:
            return JsonResponse({'status': 'error', 'message': form.errors}, status=400)

class TimeOffRequestCreateAPIView(APIView):
    def post(self, request):
        form = TimeOffRequestForm(request.POST)
        if form.is_valid():
            time_off_request = form.save(commit=False)
            time_off_request.employee_id = 1  # Assuming 1 is the employee ID
            time_off_request.save()
            return JsonResponse({'status': 'success', 'message': 'Time off request created successfully'})
        else:
            return JsonResponse({'status': 'error', 'message': form.errors}, status=400)

def my_view(request):
    employee_form = EmployeeForm()
    paystub_form = PayStubForm()
    timeoff_form = TimeOffRequestForm()
    
    context = {
        'employee_form': employee_form,
        'paystub_form': paystub_form,
        'timeoff_form': timeoff_form,
    }
    
    return render(request, 'template.html', context)
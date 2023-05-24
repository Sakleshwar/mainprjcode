from django.urls import path
from .views import *

# app_name = 'hrms'

urlpatterns = [
    path('employee/update', EmployeeUpdateAPIView.as_view(), name='employee-update'),
    path('paystub/create', PayStubCreateAPIView.as_view(), name='paystub-create'),
    path('timeoff/request', TimeOffRequestCreateAPIView.as_view(), name='timeoff-request-create'),
]

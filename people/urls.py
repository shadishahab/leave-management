from django.urls import path
from .views import EmployeeListAPI, EmployeeUpdateAPI, EmployeeRetrieveAPI, EmployeeCreateAPI

urlpatterns = [
    path('list/', EmployeeListAPI.as_view(), name='employee-list'),
    path('create/', EmployeeCreateAPI.as_view(), name='employee-create'),
    path('retrieve/<int:pk>/', EmployeeRetrieveAPI.as_view(), name='employee-retrieve'),
    path('update/', EmployeeUpdateAPI.as_view(), name='employee-update'),
    
]
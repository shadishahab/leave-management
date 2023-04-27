from django.urls import path
from .views import LeaveRequestCreateAPI, LeaveRequestUpdateAPI

urlpatterns = [
    path('create/', LeaveRequestCreateAPI.as_view(), name='leaverequest-create'),
    path('update/<int:pk>/', LeaveRequestUpdateAPI.as_view(), name='leaverequest-update')
]
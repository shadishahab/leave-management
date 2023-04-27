from .serializers import LeaveRequestCreateSerializer, LeaveRequestUpdateSerializer
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import LeaveRequest
from lib.permissions import IsEmployer
from django.utils import timezone
from .utils import PTO_calculator

class LeaveRequestCreateAPI(CreateAPIView):
    """
    Employees can send their leave request using this view
    """
    permission_classes = [IsAuthenticated]
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LeaveRequestUpdateAPI(UpdateAPIView):
    """
    Employers can approve or deny their employees' leave request using this view
    """
    permission_classes = [IsAuthenticated, IsEmployer]
    serializer_class = LeaveRequestUpdateSerializer

    def get_queryset(self):
        return LeaveRequest.objects.all()

    def perform_update(self, serializer):
        instance = serializer.save(reviewed_by=self.request.user, review_date=timezone.now())
        if instance.status == LeaveRequest.APPROVED:
            employee = instance.user.person
            requested_hours = PTO_calculator(instance.from_date, instance.to_date, instance.from_hour, instance.to_hour)
            employee.balance -= requested_hours
            employee.save()

    
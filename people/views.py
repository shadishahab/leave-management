from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from .models import Person
from .serializers import EmployeeListSerializer, EmployeeCreateSerializer, EmployeeUpdateSerializer
from rest_framework.permissions import IsAuthenticated
from lib.permissions import IsEmployer
from rest_framework.response import Response
from rest_framework import status

class EmployeeListAPI(ListAPIView):
    """
    Employers can see all of their employees using this view
    """
    permission_classes=[IsAuthenticated, IsEmployer]
    serializer_class = EmployeeListSerializer

    def get_queryset(self):
        return Person.objects.filter(company=self.request.user.person.company)

class EmployeeCreateAPI(CreateAPIView):
    queryset =  Person.objects.all()
    serializer_class = EmployeeCreateSerializer

    def perform_create(self, serializer):
        serializer.save()
        return Response({'success': 'Employee created successfully.'}, status=status.HTTP_201_CREATED)
        

class EmployeeRetrieveAPI(RetrieveAPIView):
    """
    Each employee can see their information using this view
    """
    permission_classes=[IsAuthenticated]
    queryset = Person.objects.all()
    serializer_class = EmployeeListSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)

class EmployeeUpdateAPI(UpdateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=EmployeeUpdateSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.person.is_employer:
            return qs.filter(company=self.request.user.person.company)
        return qs.filter(user=self.request.user)
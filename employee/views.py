# Create your views here.
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from employee.models import Company, Employee
from employee.serializers import CompanySerializer, EmployeeSerializer


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        company = Company.objects.get(pk=pk)
        emps = Employee.objects.filter(company=company)
        emp_serializer = EmployeeSerializer(emps, many=True, context={'request': request})

        print("get employees of", pk, "company")

        return Response(emp_serializer.data)


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
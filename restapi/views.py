from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ViewSet):
    @action(detail=True, methods=['POST'])
    def create_employee(self, request):
        """ Method to create employee"""
        try:
            serializer = EmployeeSerializer(data=request.data)
            if serializer.is_valid():
                email = serializer.validated_data.get('email')
                if Employee.objects.filter(email=email).exists():
                    return Response({'message': 'Employee already exists', 'success': False}, status=status.HTTP_200_OK)
                else:
                    serializer.save()
                    return Response({'message': 'Employee created successfully', 'success': True}, status=status.HTTP_200_OK)
            return Response({'message': 'Invalid body request', 'success': False}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': 'Employee creation failed', 'success': False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=True, methods=['PUT'])
    def update_employee(self, request):
        """ Update method to update existing employee"""
        try:
            regid = request.data.get('regid')
            if regid:
                try:
                    employee = Employee.objects.get(id=regid)
                    serializer = EmployeeSerializer(employee, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response({'message': 'Employee details updated successfully', 'success': True}, status=status.HTTP_200_OK)
                    return Response({'message': 'Invalid body request', 'success': False}, status=status.HTTP_400_BAD_REQUEST)
                except Employee.DoesNotExist:
                    return Response({'message': 'No employee found with this regid', 'success': False}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Invalid body request, regid missing', 'success': False}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': 'Employee updation failed', 'success': False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['DELETE'])
    def delete_employee(self, request):
        """ for deleting the employee"""
        try:
            regid = request.data.get('regid')
            if regid:
                try:
                    employee = Employee.objects.get(id=regid)
                    employee.delete()
                    return Response({'message': 'Employee deleted successfully', 'success': True}, status=status.HTTP_200_OK)
                except Employee.DoesNotExist:
                    return Response({'message': 'No employee found with this regid', 'success': False}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Invalid body request, regid missing', 'success': False}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': 'Employee deletion failed', 'success': False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['GET'])
    def list_employees(self, request):
        """ getting list of existing employee/employees"""
        try:
            regid = request.query_params.get('regid')
            if regid:
                try:
                    employee = Employee.objects.get(id=regid)
                    serializer = EmployeeSerializer(employee)
                    return Response({'message': 'Employee details found', 'success': True, 'employees': [serializer.data]}, status=status.HTTP_200_OK)
                except Employee.DoesNotExist:
                    return Response({'message': 'No employee found with this regid', 'success': False, 'employees': []}, status=status.HTTP_200_OK)
            else:
                employees = Employee.objects.all()
                serializer = EmployeeSerializer(employees, many=True)
                return Response({'message': 'Employee details found', 'success': True, 'employees': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': 'Error fetching employee details', 'success': False, 'employees': []}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

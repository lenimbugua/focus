from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView
)

from rest_framework import filters

from main.models import Employee
from .serializers import EmployeeSerializer

from .pagination import EmployeePageNumberPagination

#list employees, allow filter by department
class EmployeeListAPIView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('department')
    pagination_class = EmployeePageNumberPagination

#create employee 
class EmployeeCreateAPIView(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

#update employee details
class EmployeeUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

#destroy employee  
class EmployeeDestroyAPIView(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

#upload from csv endpoint
# class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     csv_file = request.FILES['file']

#     if not csv_file.name.endswith('.csv'):
#         messages.error(request, "This file is not a .csv file")

#     data_set = csv_file.read().decode('utf-8')
#     io_string = io.StringIO(data_set)
#     next(io_string)
#     for column in csv.reader(io_string, delimiter=',', quotechar="|"):
#         _, created = Contact.objects.update_or_create(
#             first_name=column[0],
#             last_name=column[1],
#             email=column[2],
#             ip_address=column[3],
#             message=column[4]
#         )
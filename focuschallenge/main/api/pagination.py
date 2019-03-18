# makes pagination, sets 10 items per page
from rest_framework.pagination import PageNumberPagination

class EmployeePageNumberPagination(PageNumberPagination):
    page_size=10
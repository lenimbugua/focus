from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from main.api import views

urlpatterns = [
    path('', views.EmployeeListAPIView.as_view()),
    # path('employees/<int:pk>/', views.EmployeeCreateA.as_view()),
    path('create/', views.EmployeeCreateAPIView.as_view()),
    path('<int:pk>/update/', views.EmployeeUpdateAPIView.as_view()),
    path('<int:pk>/destroy', views.EmployeeDestroyAPIView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
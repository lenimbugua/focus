from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
import json


# views.
def homepage(request):
    return render(request = request,
                  template_name='main/home.html',
                  context = {"employees":Employee.objects.all})

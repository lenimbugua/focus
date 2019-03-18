from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    phone = models.CharField(max_length=40, blank=True)
    department = models.CharField(max_length=40)
    employee_ID = models.CharField(max_length=40)

    def __str__(self):
        return self.first_name

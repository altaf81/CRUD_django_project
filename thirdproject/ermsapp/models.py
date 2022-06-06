from django.db import models
import re
from django.core.exceptions import ValidationError


class MyManager(models.Manager):
    def get_total_rows(self):
        row_list = super().all()
        return len(row_list)


def isage_valid(value):
    if value > 17:
        return True
    else:
        raise ValidationError('Age must be greater than 17')


def isname_valid(value):
    nformat = "^[A-Z][a-z]+$"
    if re.search(nformat, value):
        return True
    else:
        raise ValidationError('Enter valid name')


class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_name = models.CharField(max_length=50, validators=[isname_valid])
    emp_salary = models.FloatField()
    emp_Age = models.IntegerField(validators=[isage_valid])

    empmanager = models.Manager()
    empmanager2 = MyManager()

    def __str__(self):
        return f'{self.emp_id}-{self.emp_name}'


class Department(models.Model):
    dept_name = models.CharField(max_length=30)
    dept_address = models.TextField()

    class Meta:
        db_table = 'dept'

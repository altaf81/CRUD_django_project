from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    emp_name = forms.CharField(label='Employee Name', widget=forms.TextInput(attrs={
        'placeholder': 'Enter your name',
        'class': 'form-control'
    }),
        error_messages={
        'required': 'Name is compulsory'
    })
    emp_salary = forms.CharField(label='Employee Salary', widget=forms.NumberInput(attrs={
        'placeholder': 'Enter your Salary',
        'class': 'form-control'
    }),
        error_messages={
        'required': 'Salary is required'
    })

    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {'emp_Age': forms.NumberInput(attrs={'placeholder': 'Enter your Salary',
                                                       'class': 'form-control'})}

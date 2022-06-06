from django.shortcuts import redirect, render
from ermsapp.models import Employee
from .forms import EmployeeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url="/accountsapp/login")
def addemp(req):
    if req.method == 'GET':
        form = EmployeeForm()
        context = {'form': form}
        return render(req, 'ermsapp/empform.html', context)
    elif req.method == 'POST':
        form = EmployeeForm(data=req.POST)
        if form.is_valid():
            form.save()
            messages.add_message(req, messages.SUCCESS, 'Employee Added')
            return redirect('emplist')
        else:
            messages.add_message(req, messages.ERROR, 'Employee not Added')
            context = {'form': form}
            return render(req, 'ermsapp/empform.html', context)


@login_required(login_url="/accountsapp/login")
def emplist(req):
    elist = Employee.empmanager.all()
    context = {'elist': elist}
    return render(req, 'ermsapp/emplist.html', context)


def deleteemp(req, emp_id):
    emp = Employee.empmanager2.filter(emp_id=emp_id)[0]
    if req.method == 'GET':
        context = {'emp': emp}
        return render(req, 'ermsapp/confirm_delete.html', context)
    elif req.method == 'POST':
        emp.delete()
        messages.success(req, 'Employee deleted successfully')
        return redirect('emplist')


def deleteemp2(req):
    if req.method == 'GET':
        emp_id = req.GET['emp_id']
        emp = Employee.empmanager2.get(emp_id=emp_id)
        context = {'emp': emp}
        return render(req, 'ermsapp/confirm_delete2.html', context)
    elif req.method == 'POST':
        emp_id = req.POST['emp_id']
        emp = Employee.empmanager2.get(emp_id=emp_id)
        emp.delete()
        messages.success(req, 'Employee deleted successfully')
        return redirect('emplist')


def updateemp(req, emp_id):
    emp = Employee.empmanager2.get(emp_id=emp_id)
    if req.method == 'GET':
        form = EmployeeForm(instance=emp)
        context = {'form': form}
        return render(req, 'ermsapp/empform.html', context)
    if req.method == 'POST':
        form = EmployeeForm(data=req.POST, instance=emp)
        if form.is_valid():
            form.save()
            messages.success(req, 'Records updated')
            return redirect('emplist')
        else:
            messages.error(req, 'records are not updated, Try again')
            context = {'form': form}
            return render(req, 'ermsapp/empform.html', context)


def sortasc(req):
    elist = Employee.empmanager2.order_by('emp_name')
    context = {'elist': elist}
    return render(req, 'ermsapp/emplist.html', context)


def sortdesc(req):
    elist = Employee.empmanager2.order_by('-emp_name')
    context = {'elist': elist}
    return render(req, 'ermsapp/emplist.html', context)


def searchemp(req):
    q = req.GET['query']
    elist = Employee.empmanager2.filter(emp_name__icontains=q)
    context = {'elist': elist}
    return render(req, 'ermsapp/emplist.html', context)

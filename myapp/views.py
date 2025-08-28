from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm


def welcome(request):
    return render(request, "welcome.html")


def load_form(request):
    form = EmployeeForm()
    return render(request, "index.html", {'form': form})


def add(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/show')
    else:
        form = EmployeeForm()
    return render(request, "index.html", {"form": form})


def show(request):
    employee = Employee.objects.all()
    return render(request, "show.html", {'employee': employee})


def edit(request, id):
    employee = get_object_or_404(Employee, id=id)
    form = EmployeeForm(instance=employee)
    return render(request, "edit.html", {"form": form, "employee": employee})


def update(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/show')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, "edit.html", {"form": form, "employee": employee})


def delete(request, id):
    employee = get_object_or_404(Employee, id=id)
    employee.delete()
    return redirect('/show')


def search(request):
    query = request.GET.get('q')  # search box se input
    if query:
        employee = Employee.objects.filter(ename__icontains=query)  # sirf name pe search
    else:
        employee = Employee.objects.all()
    return render(request, "show.html", {'employee': employee, 'query': query})

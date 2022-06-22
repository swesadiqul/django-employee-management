import email
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from .models import *


# Create your views here.
def index(request):
    return render(request, 'index.html')

def registration(request):
    error = ""
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        employee_code = request.POST['empcode']
        email = request.POST['email']
        password = request.POST['pwd']

        try:
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=email, email=email, password=password)
            EmployeeDetail.objects.create(user=user, empcode=employee_code)
            EmployeeEducation.objects.create(user=user)
            EmployeeExperience.objects.create(user=user)
            error = "no"

        except:
            error = "yes"

    return render(request, 'registration.html', locals())


def emp_login(request):
    error = ""
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user:
            login(request, user)
            error = "no"
        else:
            error = "yes"
    return render(request, 'emp_login.html', locals())


def emp_home(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    return render(request, 'emp_home.html')

def logout_user(request):
    logout(request)
    return redirect('index')



def profile(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = request.user
    employee = EmployeeDetail.objects.get(user=user)
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        employee_code = request.POST['empcode']
        department = request.POST['department']
        designation = request.POST['designation']
        contact = request.POST['contact']
        jdate = request.POST['jdate']
        gender = request.POST['gender']

        employee.user.first_name = first_name
        employee.user.last_name = last_name
        employee.empcode = employee_code
        employee.empdept = department
        employee.designation = designation
        employee.contact = contact
        employee.gender = gender
        if jdate:
             employee.joiningdate = jdate

        try:
            employee.save()
            employee.user.save()
            error = "no"

        except:
            error = "yes"

    return render(request, 'profile.html', locals())


def admin_login(request):
    return render(request, 'admin_login.html')


def my_experience(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')

    user = request.user
    experience = EmployeeExperience.objects.get(user=user)

    return render(request, 'myexperience.html', locals())


def edit_experience(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = request.user
    experience = EmployeeExperience.objects.get(user=user)
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        employee_code = request.POST['empcode']
        department = request.POST['department']
        designation = request.POST['designation']
        contact = request.POST['contact']
        jdate = request.POST['jdate']
        gender = request.POST['gender']

        experience.user.first_name = first_name
        experience.user.last_name = last_name
        experience.empcode = employee_code
        experience.empdept = department
        experience.designation = designation
        experience.contact = contact
        experience.gender = gender

        try:
            experience.save()
            error = "no"

        except:
            error = "yes"

    return render(request, 'edit_experience.html', locals())

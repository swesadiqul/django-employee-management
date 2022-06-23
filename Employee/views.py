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

    return render(request, 'my_experience.html', locals())


def edit_myexperience(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = request.user
    experience = EmployeeExperience.objects.get(user=user)
    if request.method == 'POST':
        company1name = request.POST['company1name']
        company1desig = request.POST['company1desig']
        company1salary = request.POST['company1salary']
        company1duration = request.POST['company1duration']
        company2name = request.POST['company2name']
        company2desig = request.POST['company2desig']
        company2salary = request.POST['company2salary']
        company2duration = request.POST['company2duration']
        company3name = request.POST['company3name']
        company3desig = request.POST['company3desig']
        company3salary = request.POST['company3salary']
        company3duration = request.POST['company3duration']

        experience.company1name = company1name
        experience.company1desig = company1desig
        experience.company1salary = company1salary
        experience.company1duration = company1duration
        experience.company2name = company2name
        experience.company2desig = company2desig
        experience.company2salary = company2salary
        experience.company2duration = company2duration
        experience.company3name = company3name
        experience.company3desig = company3desig
        experience.company3salary = company3salary
        experience.company3duration = company3duration

        try:
            experience.save()
            error = "no"

        except:
            error = "yes"

    return render(request, 'edit_myexperience.html', locals())


def my_education(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')

    user = request.user
    education = EmployeeEducation.objects.get(user=user)

    return render(request, 'my_education.html', locals())


def edit_myeducation(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = request.user
    education = EmployeeEducation.objects.get(user=user)
    if request.method == 'POST':
        coursepg = request.POST['coursepg']
        schoolclgpg = request.POST['schoolclgpg']
        yearofpassingpg = request.POST['yearofpassingpg']
        percentagepg = request.POST['percentagepg']
        coursegra = request.POST['coursegra']
        schoolclggra = request.POST['schoolclggra']
        yearofpassinggra = request.POST['yearofpassinggra']
        percentagegra = request.POST['percentagegra']
        coursessc = request.POST['coursessc']
        schoolclgssc = request.POST['schoolclgssc']
        yearofpassingssc = request.POST['yearofpassingssc']
        percentagessc = request.POST['percentagessc']
        coursehsc = request.POST['coursehsc']
        schoolclghsc = request.POST['schoolclghsc']
        yearofpassinghsc = request.POST['yearofpassinghsc']
        percentagehsc = request.POST['percentagehsc']

        education.coursepg = coursepg
        education.schoolclgpg = schoolclgpg
        education.yearofpassingpg = yearofpassingpg
        education.percentagepg = percentagepg
        education.coursegra = coursegra
        education.schoolclggra = schoolclggra
        education.yearofpassinggra = yearofpassinggra
        education.percentagegra = percentagegra
        education.coursessc = coursessc
        education.schoolclgssc = schoolclgssc
        education.yearofpassingssc = yearofpassingssc
        education.percentagessc = percentagessc
        education.coursehsc = coursehsc
        education.schoolclghsc = schoolclghsc
        education.yearofpassinghsc = yearofpassinghsc
        education.percentagehsc = percentagehsc

        try:
            education.save()
            error = "no"

        except:
            error = "yes"

    return render(request, 'edit_myeducation.html', locals())

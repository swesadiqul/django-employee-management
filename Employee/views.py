import email
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
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
    return render(request, 'emp_home.html')
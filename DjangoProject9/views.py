# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from datetime import datetime
from .forms import LoginForm, StudentProfileForm, EmployeeProfileForm


def welcome(request):
    return render(request, 'welcome.html', {'current_date_time': datetime.now()})


@csrf_protect
def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect('welcome')  # Utilisation de `redirect()` plutôt que `HttpResponseRedirect`
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .forms import LoginForm

@csrf_protect
def login2(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect('welcome')  # Redirection vers la page d'accueil
    else:
        form = LoginForm()

    return render(request, 'login2.html', {'form': form})



@csrf_protect
def register(request):
    if request.method == "POST":
        form = StudentProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = StudentProfileForm()

    return render(request, 'user_profile.html', {'form': form})


@csrf_protect
def register2(request):
    studentForm = StudentProfileForm(prefix="st")
    employeeForm = EmployeeProfileForm(prefix="em")

    if request.method == "POST" and 'profileType' in request.POST:
        if request.POST['profileType'] == 'student':
            studentForm = StudentProfileForm(request.POST, prefix="st")
            if studentForm.is_valid():
                studentForm.save()
                return redirect('login')
        elif request.POST['profileType'] == 'employee':
            employeeForm = EmployeeProfileForm(request.POST, prefix="em")
            if employeeForm.is_valid():
                employeeForm.save()
                return redirect('login')

    return render(request, 'user_profile2.html',
                  {'studentForm': studentForm, 'employeeForm': employeeForm})

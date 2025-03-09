from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse
from datetime import datetime
from .forms import LoginForm  # Assure-toi d'importer correctement ton formulaire


def welcome(request):
    return render(request, 'welcome.html', {'current_date_time': datetime.now()})


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            error = "Veuillez entrer une adresse de courriel et un mot de passe."
            return render(request, 'login.html', {'error': error})

        user = authenticate(request, username=email, password=password)
        if user is None:
            error = "Adresse de courriel ou mot de passe erroné."
            return render(request, 'login.html', {'error': error})

        auth_login(request, user)  # Authentification de l'utilisateur
        return redirect('welcome')  # Redirection vers la page d'accueil

    return render(request, 'login.html')  # Affichage du formulaire si pas de POST


def login2(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user:
                auth_login(request, user)
                return redirect('welcome')
            else:
                form.add_error(None, "Adresse de courriel ou mot de passe erroné.")  # Ajoute une erreur globale

        return render(request, 'login2.html', {'form': form})  # Réaffichage avec erreurs

    form = LoginForm()
    return render(request, 'login2.html', {'form': form})

from django import forms
from django.contrib.auth import authenticate
from .models import Personne, Etudiant, Employe

class LoginForm(forms.Form):
    email = forms.EmailField(label='Courriel :', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        label='Mot de passe :',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if email and password:
            # Utilisation de Django authenticate pour la gestion des utilisateurs
            user = authenticate(username=email, password=password)
            if user is None:
                raise forms.ValidationError("Adresse de courriel ou mot de passe erroné.")

        return cleaned_data

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        exclude = ('amis',)
        widgets = {
            'date_de_naissance': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class EmployeeProfileForm(forms.ModelForm):
    class Meta:
        model = Employe
        exclude = ('amis',)
        widgets = {
            'date_de_naissance': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

from django import forms
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    email = forms.EmailField(label='Courriel :')
    password = forms.CharField(label='Mot de passe :', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if email and password:
            user = authenticate(username=email, password=password)
            if user is None:
                raise forms.ValidationError("Adresse de courriel ou mot de passe erroné.")

        return cleaned_data

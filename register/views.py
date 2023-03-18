from django.shortcuts import render
from . import forms

# Create your views here.
def register(response):
    form = forms.RegistrationForm()
    return render(response, "register/register.html", {"form": form})

# myapp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from dashboard.models import MotherHealth, FamilyPlanning, BirthsDeaths


class MotherHealthForm(forms.ModelForm):
    class Meta:
        model = MotherHealth
        fields = '__all__'


class FamilyPlanningForm(forms.ModelForm):
    class Meta:
        model = FamilyPlanning
        fields = '__all__'


class BirthsDeathsForm(forms.ModelForm):
    class Meta:
        model = BirthsDeaths
        fields = '__all__'
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    class Meta:
        model = User

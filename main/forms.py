from django import forms
from django.contrib.auth.models import User
from .models import *


class StudentForm(forms.ModelForm):

    class Meta:
        model = stud
        fields = ['name', 'webmail', 'department', 'hostel']


class FacultyForm(forms.ModelForm):

    class Meta:
        model = Faculty
        fields = ['webmail', 'department','name']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

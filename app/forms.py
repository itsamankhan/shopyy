from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django import forms
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    email = forms.CharField(label='Email', required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control'
    }))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput(attrs={
        'class': "form-control"
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {'username': forms.TextInput(attrs={'class':'form-control'})}

        

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': "form-control"
    }))


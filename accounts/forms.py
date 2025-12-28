from .models import User
from django import forms

class RegisterForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['email', 'password']

class VerifyCodeForm(forms.Form):
    code = forms.CharField(max_length=5, label="Enter the verufycation code")

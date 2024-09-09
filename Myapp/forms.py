from django import forms
class SignupForm(forms.Form):
    username=forms.CharField()
    email=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    password=confirm=forms.CharField(widget=forms.PasswordInput)
    
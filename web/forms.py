from django import forms


class RegistrationForm(forms.Form):
    email = forms.EmailField()
    username = forms.CharField()
    password = forms.CharField()
    password2 = forms.CharField()
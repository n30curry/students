from django import forms

class ALogin(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()

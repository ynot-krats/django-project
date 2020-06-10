from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Profile

class signUpForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class customers(ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class loginForm(forms.Form):
    password = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control validate', 'type': 'password', 'id': 'pass'}), max_length=30)
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control validate', 'type': 'text', 'id': 'pass'}), max_length=30)

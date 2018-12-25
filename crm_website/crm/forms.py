from django.contrib.auth.models import User
from django import forms

class UserForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
      model = User
      fields = ['username', 'password']


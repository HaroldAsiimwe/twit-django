from django import forms
import re
from .models import Account
from django.core.exceptions import ObjectDoesNotExist


class SignupForm(forms.Form):
    name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
    passwordOne = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
        )
    passwordTwo = forms.CharField(
        label='Password (Again)', 
        widget=forms.PasswordInput
        )
 
def clean_passwordTwo(self):
    if 'password1' in self.clean_data:
        passwordOne = self.clean_data['passwordOne']
        passwordTwo = self.clean_data['passwordTwo']

        if passwordOne == passwordTwo:
            return passwordTwo
    raise forms.ValidationError('Passwords do not match.')

def clean_username(self):
    username = self.clean_data['username']
    if not re.search(r'^\w+$', username):
        raise forms.ValidationError('Username can only contain alphanumeric Characters and the underscore.')
    try:
        Account.objects.get(username=username)
    except ObjectDoesNotExist:
        return username
    raise forms.ValidationError('Username is already Taken')

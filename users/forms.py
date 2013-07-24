from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import validate_email
from django.shortcuts import get_object_or_404

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
 
    def clean_password(self):
        if 'passwordOne' in self.cleaned_data:
            passwordOne = self.cleaned_data['passwordOne']
            passwordTwo = self.cleaned_data['passwordTwo']

            if passwordOne == passwordTwo:
                return passwordTwo
        raise forms.ValidationError('Passwords do not match.')

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('Username can only contain alphanumeric Characters and the underscore.')
        try:
            User.objects.get(username__exact=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('Username is already Taken')

    def validate(self, value):
        super(SignupForm, self).validate(value)
        for email in value:
            validate_email(email)
            
class TweetForm(forms.Form):
	
    tweet = forms.CharField(widget=forms.Textarea(attrs={'size': 140}), 
        error_messages={'required':'You did not send a tweet!'} )
    tweet_pic = forms.CharField(widget=forms.FileInput(), required=False)
	
    def clean_tweet(self):
        tweet = self.cleaned_data['tweet']
        if len(tweet) > 140:
            raise forms.ValidationError('Tweets can not exceed 140 characters')
        return tweet
	


    

from django import forms
from todo.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter the first name'
               }))

    last_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter the last name'
               }))

    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter the E-mail ID'
               }))

    username = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter the username'}))

    password1 = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter the password'}))

    password2 = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter the confirm '
                                                       'password'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1',
                  'password2')


class FeedbackForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter the name'}))

    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter the E-mail '
                                                       'address'}))

    choices = (
        ('5-Star', '5-Star'),
        ('4-Star', '4-Star'),
        ('3-Star', '3-Star'),
        ('2-Star', '2-Star'),
        ('1-Star', '1-Star'),
    )

    stars = forms.ChoiceField(required=True, choices=choices, widget=forms.
                              Select(attrs={'class': 'form-control'}))

    message = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'class': 'form-control', 'cols': 80, 'rows': 10,
               'placeholder': 'Enter the message..'}))

    class Meta:
        model = Feedback
        fields = ('name', 'email', 'stars', 'message')

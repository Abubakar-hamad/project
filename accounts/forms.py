from django.forms import ModelForm
from . import models
from django import forms
from django.contrib.auth.forms import UserCreationForm , UserChangeForm 
from django.contrib.auth.models import User  
from . models import Profile

class SignupForm(UserCreationForm):
    class Meta:
        model= User
        fields = ['username' , 'email' , 'password1' , 'password2']



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['country' , 'address', 'image' , 'phone_number']



class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name' , 
            'email'
        ]

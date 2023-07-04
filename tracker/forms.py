from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import transaction
from .models import Checklist
from django import forms
from django.contrib.auth import get_user_model

# class StaffRegistrationForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
    
#     class Meta:
#         model = Staff
#         fields = ['username','password','email','role']
        
        
        
# class StaffLoginForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import transaction
from .models import User, Minister, Accountant,Checklist
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class AccountantSignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())
    ID_no = forms.CharField(widget=forms.TextInput())
    staff_no = forms.CharField(widget=forms.TextInput())
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_accountant = True
        if commit:
            user.save()
        accountant = Accountant.objects.create(user=user,
                                               first_name=self.cleaned_data.get('first_name'), 
                                               last_name=self.cleaned_data.get('last_name'), 
                                               ID_no=self.cleaned_data.get('ID_no'),
                                               staff_no=self.cleaned_data.get("staff_no"))
        return user
    
    
    
class MinisterSignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())
    ID_no = forms.CharField(widget=forms.TextInput())
    ministry = forms.CharField(widget=forms.TextInput())
    

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_minister = True
        if commit:
            user.save()
        minister = Minister.objects.create(user=user, first_name=self.cleaned_data.get('first_name'), last_name=self.cleaned_data.get('last_name'), ID_no=self.cleaned_data.get('ID_no'),ministry=self.cleaned_data.get('ministry'))
        return user


class LoginForm(AuthenticationForm):
    # email= forms.CharField(widget=forms.TextInput())
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    

from django import forms
from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = [ 
            # 'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
            'is_staff',]
    
    def save(self,commit=True):
        user = super().save(commit=False)
        # user.email=self.cleaned_data['email']
        if commit:
            user.save()
        return user


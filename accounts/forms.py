from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms

from django.forms.widgets import PasswordInput, TextInput

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1','password2']

    def __init__(self,*args,**kwargs):
        super(CreateUserForm, self).__init__(*args,**kwargs)

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if User.objet.filter(email=email).exists():
            raise forms.ValidationError('this email is invalid')
        if len(email)>=350:
            raise forms.ValidationError('your email is too long')

        # self.fields['email'].required = True

class LoginForm(AuthenticationForm):
    pass

class UpdateUserForm(forms.ModelForm):
    pass 

from django.forms import ModelForm
from django import forms
from App_Login.models import UserProfile

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('email','username', 'password1', 'password2',)

class UserProfileChange(UserChangeForm):
    class Meta:
        model=User
        fields=('username', 'email', 'first_name', 'last_name', 'password')

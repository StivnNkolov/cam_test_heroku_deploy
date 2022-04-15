from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import forms as auth_forms

from cam_0504.accounts.models import Profile


class UserRegisterForm(auth_forms.UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'password1', 'password2']


class UserLogInForm(auth_forms.AuthenticationForm):
    pass


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'age', 'city_name', 'email', 'restaurant_name']


class ChangeUserPasswordForm(auth_forms.PasswordChangeForm):
    pass


class ProfileDeleteForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = []

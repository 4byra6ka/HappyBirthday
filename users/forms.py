from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import User


class UserLoginForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': "Логин", 'class': 'form-control', 'type': 'username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'placeholder': "Пароль", 'class': 'form-control', 'type': 'password'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs={'placeholder': "", 'class': 'form-control', 'type': 'username'}))
    email = forms.EmailField(label='Почта', widget=forms.EmailInput(
        attrs={'placeholder': "", 'class': 'form-control', 'type': 'email'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(
        attrs={'placeholder': "", 'class': 'form-control', 'type': 'first_name'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(
        attrs={'placeholder': "", 'class': 'form-control', 'type': 'last_name'}))
    birthday = forms.DateField(label='', widget=forms.DateInput(
        attrs={'placeholder': "DD/MM/YYYY", 'class': 'form-control', 'type': 'birthday'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'placeholder': "", 'class': 'form-control', 'type': 'password'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(
        attrs={'placeholder': "", 'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'birthday', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    email = forms.EmailField(label='Почта', widget=forms.EmailInput(
        attrs={'placeholder': "", 'class': 'form-control', 'type': 'email_edit'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(
        attrs={'placeholder': "", 'class': 'form-control', 'type': 'first_name'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(
        attrs={'placeholder': "", 'class': 'form-control', 'type': 'last_name'}))
    birthday = forms.DateField(label='', widget=forms.DateInput(
        attrs={'placeholder': "DD/MM/YYYY", 'class': 'form-control', 'type': 'birthday'}))
    telegram = forms.IntegerField(label='Фамилия', widget=forms.NumberInput(
        attrs={'placeholder': "", 'class': 'form-control', 'type': 'telegram'}), required=False)
    is_staff = forms.BooleanField(label='Модератор', widget=forms.CheckboxInput(
        attrs={ 'class': 'form-check-input', 'type': 'checkbox'}), required=False)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'birthday', 'telegram', 'is_staff')


class UserRecoveryPasswordForm(forms.Form):
    username_recovery = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs={'placeholder': "", 'class': 'form-control', 'type': 'username_recovery'}))

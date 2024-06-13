from django import forms

from employees.models import Employees


class EmployeesCreateForm(forms.ModelForm):
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(
        attrs={'placeholder': "", 'class': 'form-control', 'type': 'first_name_create'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(
        attrs={'placeholder': "", 'class': 'form-control', 'type': 'last_name'}))
    birthday = forms.DateField(label='', widget=forms.DateInput(
        attrs={'placeholder': "DD/MM/YYYY", 'class': 'form-control', 'type': 'birthday'}))
    email = forms.EmailField(label='Почта', widget=forms.EmailInput(
        attrs={'placeholder': "", 'class': 'form-control', 'type': 'email'}))
    telegram = forms.IntegerField(label='Фамилия', widget=forms.NumberInput(
        attrs={'class': 'form-control', 'type': 'telegram'}), required=False)

    class Meta:
        model = Employees
        fields = ('first_name', 'last_name', 'birthday', 'email', 'telegram')

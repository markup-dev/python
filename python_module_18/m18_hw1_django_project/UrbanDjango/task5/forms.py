from django import forms


class UserRegister(forms.Form):
	username = forms.CharField(label='Введите логин:', min_length=3, max_length=30)
	password = forms.CharField(label='Введите пароль:', widget=forms.PasswordInput, min_length=8, max_length=30)
	repeat_password = forms.CharField(label='Повторите пароль:', widget=forms.PasswordInput, min_length=8, max_length=30)
	age = forms.IntegerField(label='Введите свой возраст:')

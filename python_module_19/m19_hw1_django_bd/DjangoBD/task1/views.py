# from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import *


# Create your views here.
def platform_view(request):
	title = 'Главная страница'
	context = {
		'title': title
	}
	return render(request, 'first_task/platform.html', context)


def games_view(request):
	title = 'Игры'
	games = Game.objects.all()
	context = {
		'title': title,
		'games': games.values()
	}
	return render(request, 'first_task/games.html', context)


def cart_view(request):
	title = 'Корзина'
	text = 'Извините, ваша корзина пуста'
	context = {
		'title': title,
		'text': text
	}
	return render(request, 'first_task/cart.html', context)


def sign_up_by_html(request):
	info = {}

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		repeat_password = request.POST.get('repeat_password')
		age = request.POST.get('age')

		if password != repeat_password:
			info['error'] = 'Пароли не совпадают'
		elif int(age) < 18:
			info['error'] = 'Вы должны быть старше 18'
		elif Buyer.objects.filter(name=username).exists():
			info['error'] = 'Пользователь уже существует'
		else:
			Buyer.objects.create(name=username, balance=10, age=age)
			return redirect('platform/')
			# return HttpResponse(f'Приветствуем, {username}!')

	return render(request, 'first_task/registration_page.html', {'error': info.get('error')})

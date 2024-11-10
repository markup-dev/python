from django.shortcuts import render


# Create your views here.
def platform_view(request):
	title = 'Главная страница'
	context = {
		'title': title
	}
	return render(request, 'third_task/platform.html', context)


def games_view(request):
	title = 'Игры'
	games = {'Atomic Heart': 2500, 'Cyberpunk 2077': 3000, 'PayDay 2': 1500}
	context = {
		'title': title,
		'games': games
	}
	return render(request, 'third_task/games.html', context)


def cart_view(request):
	title = 'Корзина'
	text = 'Извините, ваша корзина пуста'
	context = {
		'title': title,
		'text': text
	}
	return render(request, 'third_task/cart.html', context)

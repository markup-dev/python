from django.shortcuts import render


# Create your views here.
def platform_view(request):
	title = 'Главная страница'
	context = {
		'title': title
	}
	return render(request, 'fourth_task/platform.html', context)


def games_view(request):
	title = 'Игры'
	games = {'games': ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']}
	context = {
		'title': title,
		'games': games
	}
	return render(request, 'fourth_task/games.html', context)


def cart_view(request):
	title = 'Корзина'
	text = 'Извините, ваша корзина пуста'
	context = {
		'title': title,
		'text': text
	}
	return render(request, 'fourth_task/cart.html', context)

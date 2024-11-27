from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post


def post_list(request):
	post_list = Post.objects.all().order_by('-created_at')  # Упорядочиваем по дате создания (по убыванию)
	paginator = Paginator(post_list, 3)  # Показывать 5 постов на странице

	page_number = request.GET.get('page')
	page_posts = paginator.get_page(page_number)

	return render(request, 'blog/post_list.html', {'page_posts': page_posts})


# def post_list(request):
# 	post_list = Post.objects.all()
#
# 	# Получаем количество элементов на странице из параметров запроса или используем значение по умолчанию (5)
# 	items_per_page = request.GET.get('items_per_page', 5)
#
# 	paginator = Paginator(post_list, items_per_page)  # Используем выбранное количество постов на странице
#
# 	page_number = request.GET.get('page')
# 	page_posts = paginator.get_page(page_number)
#
# 	return render(request, 'blog/post_list.html', {'page_posts': page_posts})

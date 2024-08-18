import requests

# Основные функции библиотеки requests
# GET-запросы: Используются для получения данных с сервера.
# POST-запросы: Используются для отправки данных на сервер.
# PUT-запросы: Используются для обновления данных на сервере.
# DELETE-запросы: Используются для удаления данных на сервере.
# HEAD-запросы: Используются для получения мета-данных о ресурсе без загрузки самого ресурса.
# OPTIONS-запросы: Используются для получения информации о поддерживаемых методах HTTP для ресурса.

# получение жанра музыки с помощью GET
THE_URL = 'https://binaryjazz.us/wp-json/genrenator/v1/genre/'
response = requests.get(THE_URL).json()
print(response)

# Отправляем GET-запрос на сайт google.com
response = requests.get('https://www.google.com')
# Печатаем статус код ответа
print(response.status_code)
# Печатаем содержимое ответа
print(response.text)

# Данные для отправки
data = {'key': 'value'}
# Отправляем POST-запрос на сайт example.com
response = requests.post('https://www.example.com', data=data)
# Печатаем статус код ответа
print(response.status_code)
# Печатаем содержимое ответа
print(response.text)

# Параметры для запроса
params = {'key': 'API_KEY', 'text': 'Hello', 'lang': 'en-es'}
# Отправляем GET-запрос на сайт example.com с параметрами
response = requests.get('https://www.example.com', params=params)
# Печатаем статус код ответа
print(response.status_code)
# Печатаем содержимое ответа
print(response.text)

# Отправляем HEAD-запрос на сайт google.com
response = requests.head('https://www.google.com')
# Печатаем статус код ответа
print(response.status_code)
# Печатаем заголовки ответа
print(response.headers)

# Обработка ошибок при отправке запросов:
try:
	# Отправляем GET-запрос на сайт google.com
	response = requests.get('https://www.google.com')
	response.raise_for_status()  # Проверяем статус код ответа
except requests.exceptions.HTTPError as errh:
	print(f"HTTP Error: {errh}")
except requests.exceptions.ConnectionError as errc:
	print(f"Error Connecting: {errc}")
except requests.exceptions.Timeout as errt:
	print(f"Timeout Error: {errt}")
except requests.exceptions.RequestException as err:
	print(f"Something went wrong: {err}")
else:
	# Печатаем содержимое ответа
	print(response.text)

# Потоковая передача данных полезна для обработки больших объемов данных без загрузки их в память:
print("Testing `requests` library with streaming...")

resp = requests.get('https://httpbin.org/stream/10', stream=True)

for chunk in resp.iter_content(chunk_size=1024):
	print(chunk.decode('utf-8'))

# ----------------------------------
print(f'\n\n\n')

# Библиотека NumPy в Python предназначена для работы с многомерными массивами и обеспечивает высокую производительность
# при выполнении численных вычислений. Вот несколько простых примеров использования NumPy:

import numpy as np

# 1. Создание массивов
# Создание одномерного массива
array_1d = np.array([1, 2, 3, 4, 5])
print(array_1d)
# Создание двумерного массива
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(array_2d)

# 2. Индексация и срезы
# Создание двумерного массива
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
# Вывод второго элемента первого ряда
print(array_2d[0, 1])  # Выводит
# Вывод второго ряда
print(array_2d[1, :])  # Выводит [4 5 6]
# Вывод второго столбца
print(array_2d[:, 1])  # Выводит [2 5]

# 3. Основные математические операции
# Создание двух массивов
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
# Сложение массивов
print(np.add(array1, array2))  # Выводит [5 7 9]
# Умножение массивов
print(np.multiply(array1, array2))  # Выводит [4 10 18]

# 4. Статистические функции
# Создание массива
array = np.array([1, 2, 3, 4, 5])
# Среднее значение
print(np.mean(array))  # Выводит 3.0
# Медиана
print(np.median(array))  # Выводит 3.0
# Стандартное отклонение
print(np.std(array))  # Выводит 1.4142135623730951

# 5. Перестановка массивов
# Создание массива
array = np.array([[1, 2, 3], [4, 5, 6]])
# Перестановка массива в строку
print(array.flatten())  # Выводит [1 2 3 4 5 6]
# Перестановка массива в столбец
print(array.reshape(-1, 1))  # Выводит [#
																				#
																				#
																				#
																				#
																				#]

# Эти примеры демонстрируют основные возможности библиотеки NumPy, включая создание и манипуляцию массивами, выполнение
# математических операций и статистических функций.

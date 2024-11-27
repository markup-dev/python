from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from crud_functions import initiate_db, get_all_products, add_products, add_user, is_included

initiate_db()
# add_products()


products = get_all_products()

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton(text='Рассчитать'),
			KeyboardButton(text='Информация')
		],
		[KeyboardButton(text='Купить')],
		[KeyboardButton(text='Регистрация')]
	], resize_keyboard=True
)

kb_inline = InlineKeyboardMarkup(
	inline_keyboard=[
		[InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')],
		[InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')]
	], resize_keyboard=True
)

inline_menu = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text='Product1', callback_data='product_buying'),
			InlineKeyboardButton(text='Product2', callback_data='product_buying'),
			InlineKeyboardButton(text='Product3', callback_data='product_buying'),
			InlineKeyboardButton(text='Product4', callback_data='product_buying')
		]
	], resize_keyboard=True
)


class UserState(StatesGroup):
	age = State()
	growth = State()
	weight = State()


class RegistrationState(StatesGroup):
	username = State()
	email = State()
	age = State()
	balance = 1000


@dp.message_handler(text='Регистрация')
async def sing_up(message):
	await message.answer('Введите имя пользователя (только латинский алфавит):')
	await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
	if is_included(message.text):
		await message.answer('Пользователь существует, введите другое имя')
		await RegistrationState.username.set()
	else:
		await state.update_data(username=message.text)
		await message.answer('Введите свой email:')
		await RegistrationState.email.set()


@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
	await state.update_data(email=message.text)
	await message.answer('Введите свой возраст:')
	await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
	await state.update_data(age=message.text)
	data = await state.get_data()
	add_user(data['username'], data['email'], data['age'])
	await message.answer('Регистрация прошла успешно!')
	await state.finish()


@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
	await message.answer('Выберите опцию:', reply_markup=kb_inline)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
	await call.message.answer('10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')
	await call.answer()


# @dp.message_handler(commands=['start'])
# # async def start(message):
# # 	await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)

# 1 - 1
# @dp.message_handler(commands=['start'])
# async def start(message):
# 	bot_info = await bot.get_me()
# 	await message.answer(
# 		'<b>Привет, {0.first_name}!</b> Я {1.first_name}, '
# 		'и я умею выделять текст полужирным.'.format(message.from_user,bot_info),
# 		parse_mode='HTML')

# 1 - 2
# @dp.message_handler(commands=['start'])
# async def start(message):
# 	bot_info = await bot.get_me()
# 	await message.answer(
# 		'<b>Привет, {0.first_name}!</b> Я {1.first_name}, '
# 		'и я умею выделять текст полужирным, '
# 		'а еще <s>зачеркнутым</s> и <u>подчеркнутым</u>.'.format(
# 			message.from_user,
# 			bot_info),
# 		parse_mode='HTML')

# 1 - 3
# @dp.message_handler(commands=['start'])
# async def start(message):
# 	bot_info = await bot.get_me()
# 	await message.answer(
# 		'<b>Привет, {0.first_name}!</b> Я {1.first_name}, '
# 		'и я умею выделять текст полужирным, '
# 		'а еще <s>зачеркнутым</s> и <u>подчеркнутым</u>.'.format(
# 			message.from_user,
# 			bot_info),
# 		parse_mode='HTML')
# 	await message.answer(
# 		'''<pre>А этот текст отформатирован
# с сохранением   всех пробелов    и
# переносов строк</pre>''',
# 		parse_mode='HTML')
# 	await message.answer(
# 		'Посетите <a href="https://cyber.sports.ru/tribuna/blogs/gamesherald/2931119.html">эту страницу</a> '
# 		'для получения просвящения.', parse_mode='HTML')


# 2
@dp.message_handler(commands=['about'])
async def about(message):
	bot_info = await bot.get_me()
	await message.answer('<b>Привет, </b><strong>{0.first_name}</strong>! \n'
											 '<em><u>Я могу:</u></em>\n'
											 '1. Продать вам бананы\n'
											 '2. Посчитать вам калории\n'
											 '3. Зарегистрировать вас\n'
											 'и я работаю, СЛАВА <s>МОНОЛИТУ</s>'.format(
		message.from_user,
		bot_info),
		parse_mode='HTML')


@dp.message_handler(commands=['contacts'])
async def contacts(message):
	bot_info = await bot.get_me()
	await message.answer('<strong>Контакты разработчика:</strong>\n'
											 'Телефон: <tg-spoiler>+7 999 773 27 15</tg-spoiler>\n'
											 'Почта: <a href="mailto:zabiryuchenko.kristina@gmail.com">zabiryuchenko.kristina@gmail.com</a>'.format(
		message.from_user,
		bot_info),
		parse_mode='HTML')


@dp.message_handler(commands=['info'])
async def info(message):
	bot_info = await bot.get_me()
	await message.answer(
		'<ins>Фанатики</ins>. Типичные. Во что б они там ни верили, только постоянно прут в бой. '
		'А отступать вообще не умеют, даже перед превосходящими силами... '
		'это если нам удаётся пяток монолитовцев <i>зажать</i>, потому что обычно они нас жмут. '
		'У них постоянно идут подкрепления со стороны ЧАЭС, <b>понимаешь</b>?! Говнюки чёртовы... Нас и так немного было, '
		'а они ещё нескольких ребят положили'.format(
			message.from_user,
			bot_info),
		parse_mode='HTML')


@dp.message_handler(commands=['citata'])
async def citata(message):
	bot_info = await bot.get_me()
	await message.answer(
		'<pre><tg-spoiler>MONOLITH</tg-spoiler>\n'
		'Благодарим Тебя за то, что раскрыл слугам Твоим козни врагов наших! '
		'Озари сиянием Твоим души тех, кто отдал жизнь во исполнение воли Твоей! '
		'В бой, защитники Монолита! В бой! '
		'Отомстим за павших братьев наших, да будет благословенно вечное их единение с Монолитом! '
		'Смерть… лютая смерть тем, кто отвергает Его священную силу!..</pre>'.format(
			message.from_user,
			bot_info),
		parse_mode='HTML')


@dp.message_handler(commands=['help'])
async def help_command(message):
	bot_info = await bot.get_me()
	await message.answer(
		'<strong>Доступные команды:</strong>\n'
		'/about - Узнать о боте\n'
		'/contacts - Контакты разработчика\n'
		'/info - Информация о фанатиках\n'
		'/citata - Цитата <tg-spoiler><u>Монолита</u></tg-spoiler>\n'
		'/link - Полезная ссылка\n'
		'/help - Показать это сообщение\n'
		'Если у вас есть вопросы, просто напишите мне!'.format(message.from_user,
		bot_info),
		parse_mode='HTML'
	)


@dp.message_handler(commands=['link'])
async def link(message):
	bot_info = await bot.get_me()
	await message.answer('<strike>Просветитесь</strike> '
											 '<a href="https://stalker.fandom.com/ru/wiki/Монолит_(группировка)">monolith</a>'.format(
		message.from_user,
		bot_info),
		parse_mode='HTML')


@dp.message_handler(commands=['help'])
async def help_command(message):
	bot_info = await bot.get_me()
	await message.answer(
		'<strong>Доступные команды:</strong>\n'
		'/about - Узнать о боте\n'
		'/contacts - Контакты разработчика\n'
		'/info - Информация о фанатиках\n'
		'/citata - Цитата <tg-spoiler><u>Монолита</u></tg-spoiler>\n'
		'/help - Показать это сообщение\n'
		'Если у вас есть вопросы, просто напишите мне!'.format(message.from_user,
																													 bot_info),
		parse_mode='HTML'
	)


@dp.message_handler(commands=['joke'])
async def joke(message):
	bot_info = await bot.get_me()
	await message.answer('<em>Вот вам шутка:</em>\n'
											 '<strong>Почему сталкер всегда берет с собой компас? '
											 'Чтобы не заблудиться в своих мыслях!</strong>'.format(
		message.from_user, bot_info), parse_mode='HTML')

# 3
@dp.message_handler(commands=['hobby1'])
async def hobby1(message):
	bot_info = await bot.get_me()
	await message.answer('<pre>'
											 'Основные правила волейбола включают следующие моменты:\n'
											 'Игра проходит между двумя командами, каждая из которых состоит из шести игроков.'
											 'Мяч должен быть подан с одной стороны сетки на другую, и команды могут касаться мяча не более трех раз, прежде чем отправить его обратно.'
											 'Очко зарабатывается, когда мяч касается площадки соперника или когда соперник делает ошибку.'
											 'Игра ведется до трех выигранных сетов, при этом каждый сет заканчивается, когда одна команда наберет 25 очков (при условии, что разница в счете составляет минимум два очка).</pre>'.format(message.from_user, bot_info), parse_mode='HTML')

# -----------------------------------------------------
@dp.message_handler(text=['Купить'])
async def get_buying_list(message):
	for i in range(len(products)):
		await message.answer(f'Название: {products[i][1]} | Описание: {products[i][2]} | Цена: {products[i][3]}')
		with open(f'files/banan{i + 1}.png', 'rb') as img:
			await message.answer_photo(img, 'Выберите продукт для покупки:', reply_markup=inline_menu)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
	await call.message.answer('Вы успешно приобрели продукт!')
	await call.answer()


@dp.callback_query_handler(text=['calories'])
async def set_age(call):
	await call.message.answer('Введите свой возраст:')
	await UserState.age.set()
	await call.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
	await state.update_data(age=message.text)
	await message.answer('Введите свой рост:')
	await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
	await state.update_data(growth=message.text)
	await message.answer('Введите свой вес:')
	await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
	await state.update_data(weight=message.text)
	data = await state.get_data()
	norm = 10 * int(data['weight']) + 6.25 * float(data['growth']) - 5 * int(data['age']) + 5
	await message.answer(f'Ваша норма калорий {norm}')
	await state.finish()


@dp.message_handler()
async def all_messages(message):
	await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)

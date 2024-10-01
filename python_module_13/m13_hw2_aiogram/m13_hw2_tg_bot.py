from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup()
btn_calc = KeyboardButton(text='Рассчитать')
btn_info = KeyboardButton(text='Информация')

kb.add(btn_calc, btn_info)

kb.resize_keyboard = True

kb_inline = InlineKeyboardMarkup()

btn1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
btn2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')

kb_inline.add(btn1, btn2)

kb_inline.resize_keyboard = True


@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
	await message.answer('Выберите опцию:', reply_markup=kb_inline)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
	await call.message.answer('10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')
	await call.answer()


class UserState(StatesGroup):
	age = State()
	growth = State()
	weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
	await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


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

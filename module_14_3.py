from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text="Расчитать")
button2 = KeyboardButton(text="Информация")
button3 = KeyboardButton(text="Купить")
button_start = KeyboardButton(text="/start")
kb.add(button_start)
kb.row(button, button2, button3)
inlkb = InlineKeyboardMarkup(resize_keyboard=True)
inlbut1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='Расчёт')
inlbut2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
inlkb.row(inlbut1, inlbut2)
inlkb_now = InlineKeyboardMarkup(resize_keyboard=True)
inlbut1_now = InlineKeyboardButton(text='Product1', callback_data='product_buying')
inlbut2_now = InlineKeyboardButton(text='Product2', callback_data='product_buying')
inlbut3_now = InlineKeyboardButton(text='Product3', callback_data='product_buying')
inlbut4_now = InlineKeyboardButton(text='Product4', callback_data='product_buying')
inlkb_now.row(inlbut1_now, inlbut2_now, inlbut3_now, inlbut4_now)


class UserState(StatesGroup):
    age, growth, weight, gender, activity = [State() for _ in range(5)]


@dp.message_handler(text="Купить")
async def get_buying_list(message):
    for i in range(1, 5):
        with open(f'{i}.png', "rb") as img:
            await message.answer(f'Название: Product{i} | Описание: описание {i} | Цена: {i * 100}')
            await message.answer_photo(img)
    await message.answer('Выберите продукт для покупки:', reply_markup=inlkb_now)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!', reply_markup=kb)


@dp.message_handler(text='Расчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=inlkb)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('для мужчин: (10 x вес (кг) + 6.25 x рост (см) – 5 x возраст (г) + 5) x A\n'
                              'для женщин: (10 x вес (кг) + 6.25 x рост (см) – 5 x возраст (г) – 161) x A\n'
                              'где А - ваша активность')
    await call.answer()


@dp.callback_query_handler(text='Расчёт')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await call.answer()
    await UserState.age.set()


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
async def set_gender(message, state):
    await state.update_data(weight=message.text)
    await message.answer('Введите свой пол (мужской - 1, женский - 2):\n(отправьте цифру)')
    await UserState.gender.set()


@dp.message_handler(state=UserState.gender)
async def set_activity(message, state):
    await state.update_data(gender=message.text)
    await message.answer('''Введите свою активность: 
1. Минимальная активность
2. Слабая активность
3. Средняя активность
4. Высокая активность
5. Экстра-активность
(отправьте цифру)''')
    await UserState.activity.set()


@dp.message_handler(state=UserState.activity)
async def send_calories(message, state):
    await state.update_data(activity=message.text)
    data = await state.get_data()
    for k, v in data.items():
        try:
            data[k] = int(v)
        except ValueError:
            k_rus = {'age': 'возраст', 'growth': 'рост', 'weight': 'вес',
                     'gender': 'пол', 'activity': 'активность', }
            await message.answer(f'Параметр "{k_rus[k]}" должен быть числом. Вы ввели "{v}"\n'
                                 'Введите данные заново (нажмите кнопку "Расчитать")', reply_markup=kb)
            await state.finish()
            return

    activity_cases = {1: 1.2, 2: 1.375, 3: 1.55, 4: 1.725, 5: 1.9}
    user_activity = activity_cases[data['activity']]
    user_gender = -161 if int(data['gender']) - 1 else 5  # True - female, False - male

    calories = 10 * data['weight'] + 6.25 * data['growth'] - 5 * data['age']
    pro_calories = (calories + user_gender) * user_activity
    await message.answer(f'Ваша норма калорий {pro_calories}')
    await state.finish()
    await main_menu(message)


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(f'Добро пожаловать {message.from_user.username}!\n'
                         f'Привет! Я бот помогающий твоему здоровью.\n'
                         f'Для расчета Вашей потребности в калориях нажмите кнопку "Расчитать"'
                         f'Для покупки витаминов нажмите кнопку "Купить"', reply_markup=kb)


@dp.message_handler()
async def all_message(message):
    await message.answer('Нажмите кнопку /start, чтобы начать общение.', reply_markup=kb)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
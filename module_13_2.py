import aiogram
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio


api = "8049369742:AAFNS50Fy_5h_T_wcYqf2x0P-F3hVHt8MIs"
bot = aiogram.Bot(token=api)
dp = aiogram.Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message):
    print('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler()
async def all_message(message):
    print('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
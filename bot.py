import logging

from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils.executor import start_webhook

API_TOKEN = 'BOT_TOKEN_HERE'

# Настройка Webhook
WEBHOOK_HOST = 'https://a120-95-25-161-16.ngrok-free.app' # -> Адрес сервера
WEBHOOK_PATH = ''# -> Путь до api, где слушает бот
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}' # -> URL на который будут приниматься запросы

# Настройка web-сервера
WEBAPP_HOST = 'localhost' # -> хост нашего приложения, оставляем локальным
WEBAPP_PORT = 8000 # -> port на котором работает наше приложение

logging.basicConfig(level=logging.INFO)

bot = Bot(token='6261025312:AAGVVr4uPV7YBZIQ33RqXGr87YtoDzfbBYc')
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)

async def on_shutdown(dp):
    logging.warning('Shutting down...')
    await bot.delete_webhook()
    logging.warning('Bye!')

@dp.message_handler(commands=['start'])
async def echo(msg: types.Message):
    return SendMessage(msg.chat.id, msg.text)

@dp.message_handler(commands=['help'])
async def echo(msg: types.Message):
    return SendMessage(msg.chat.id, 'Вы обратились к справке бота')

if __name__ == "__main__":
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )

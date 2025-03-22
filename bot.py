import asyncio
import google.generativeai as genai
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import logging
import os

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Настройка Gemini
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyCVgQH4p3sAnaOsbR-ajuL_xFVzKh4WNU8")
genai.configure(api_key=GEMINI_API_KEY)

# 🔥 Используем актуальную модель из вашего списка
model = genai.GenerativeModel("gemini-1.5-pro-latest")  # Поддерживает текстовые запросы

# Настройка бота
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "1895077818:AAHRVL99uz_uEc_cJ4tvXti1V3nB-d_ZF4I")
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Good^morning ..Bro) lets try to get a more money!")

@dp.message()
async def handle_message(message: types.Message):
    try:
        response = model.generate_content(message.text)
        await message.answer(response.text)
    except Exception as e:
        logger.error(f"Ошибка: {e}")
        await message.answer("Произошла ошибка. Попробуйте еще раз.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
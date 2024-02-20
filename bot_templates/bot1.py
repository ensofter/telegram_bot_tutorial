import asyncio
import os
from contextlib import suppress

from aiogram import Bot, Dispatcher, F
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from dotenv import load_dotenv

import keyboard

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = Bot(TOKEN, parse_mode="HTML")
dp = Dispatcher()

smiles = [
    ["🥑", "я люблю авокадо"],
    ["🍓", "я люблю клубнику"],
    ["☔️", "я ненавижу дождь"],
    ["💩", "я покакол"],
]


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Helol, AIOgram 3.x", reply_markup=keyboard.main_kb)


@dp.callback_query(keyboard.Pagination.filter(F.action.in_(["prev", "next"])))
async def pagination_handler(call: CallbackQuery, callback_data: keyboard.Pagination):
    page_num = int(callback_data.page)
    page = page_num - 1 if page_num > 0 else 0

    if callback_data.action == "next":
        page = page_num + 1 if page_num < (len(smiles) - 1) else page_num

    with suppress(TelegramBadRequest):
        await call.message.edit_text(
            f"{smiles[page][0]} <strong>{smiles[page][1]}</strong>",
            reply_markup=keyboard.paginator(page)
        )
    await  call.answer()


@dp.message(F.text.lower().in_(["хай", "хэллоу", "привет"]))
async def greetings(message: Message):
    await message.answer("Вот тут находится ближайшая точка")
    await message.reply_location(latitude=59.942187, longitude=30.413371)


@dp.message()
async def echo(message: Message):
    msg = message.text.lower()

    if msg == 'ссылки':
        await message.answer("Вот ваши ссылки", reply_markup=keyboard.links_kb)
    elif msg == 'спец. кнопки':
        await message.answer("Спец. кнопки", reply_markup=keyboard.spec_kb)
    elif msg == 'калькулятор':
        await message.answer("Введите выражение", reply_markup=keyboard.calc_kb())
    elif msg == 'смайлики':
        await message.answer(f"{smiles[0][0]} <strong>{smiles[0][1]}</strong>", reply_markup=keyboard.paginator())


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


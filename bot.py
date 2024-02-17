import asyncio
import os
import random

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandObject
from aiogram.types import Message
from aiogram.enums.dice_emoji import DiceEmoji
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = Bot(TOKEN, parse_mode="HTML")
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(f"Helol, <strong>{message.from_user.first_name}</strong>")


@dp.message(Command(commands=["rn", "random_number"]))
async def get_random_number(message: Message, command: CommandObject):
    start, end = 1, 10
    if command.args is not None:
        start, end = map(int, command.args.split('-'))
    await message.reply(f"this is your random int:{random.randint(start, end)}")

@dp.message(F.text == "play")
async def play_game(message: Message):
    await message.answer_dice(DiceEmoji.DICE)


@dp.message()
async def echo(message: Message):
    await message.answer(f"I dont understand U")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())


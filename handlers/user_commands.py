from random import randint

from aiogram import Router
from aiogram.filters import CommandStart, CommandObject, Command
from aiogram.types import Message

from keyboards import reply

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer("Helol, AIOgram 3.x", reply_markup=reply.main)


@router.message(Command(commands=["rn", "random_number"]))
async def get_random_number(message: Message, command: CommandObject):
    start, end = 1, 10
    if command.args is not None:
        start, end = map(int, command.args.split('-'))
    await message.reply(f"this is your random int:{randint(start, end)}")

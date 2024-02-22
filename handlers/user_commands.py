from random import randint

from aiogram import Router
from aiogram.filters import CommandStart, CommandObject, Command
from aiogram.types import Message

from keyboards import reply

from filters.is_admin import IsAdmin
from filters.is_digit_or_float import IsDigitOrFloat

router = Router()


@router.message(CommandStart(), IsAdmin([82429730]))
async def start(message: Message):
    await message.answer(f"Helol, AIOgram 3.x, {message.from_user.id}", reply_markup=reply.main)


@router.message(Command('pay'), IsDigitOrFloat())
async def pay(message: Message, command: CommandObject):
    await message.answer("Вы успешно оплатили товар")


@router.message(Command(commands=["rn", "random_number"]))
async def get_random_number(message: Message, command: CommandObject):
    start, end = 1, 10
    if command.args is not None:
        start, end = map(int, command.args.split('-'))
    await message.reply(f"this is your random int:{randint(start, end)}")

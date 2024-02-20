from aiogram import Router, F
from aiogram.types import Message

from data.subloader import get_json
from keyboards import inline, builders, fabrics

router = Router()


@router.message(F.text.lower().in_(["хай", "хэллоу", "привет"]))
async def greetings(message: Message):
    await message.answer("Вот тут находится ближайшая точка")
    await message.reply_location(latitude=59.942187, longitude=30.413371)


@router.message()
async def echo(message: Message):
    msg = message.text.lower()
    smiles = await get_json("smiles.json")

    if msg == 'ссылки':
        await message.answer("Вот ваши ссылки", reply_markup=inline.links)
    elif msg == 'спец. кнопки':
        await message.answer("Спец. кнопки", reply_markup=inline.links)
    elif msg == 'калькулятор':
        await message.answer("Введите выражение", reply_markup=builders.calc_kb())
    elif msg == 'смайлики':
        await message.answer(f"{smiles[0][0]} <strong>{smiles[0][1]}</strong>", reply_markup=fabrics.paginator())

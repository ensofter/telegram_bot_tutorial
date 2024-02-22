from aiogram import BaseMiddleware
from aiogram.types import Message

from keyboards.inline import sub_channel


class CheckSubscription(BaseMiddleware):
    async def __call__(self, handler, event: Message, data):
        chat_member = await event.bot.get_chat_member("@ohtyane", event.from_user.id)
        if chat_member.status == "left":
            await event.answer("Подпишись на канал", reply_markup=sub_channel)
        else:
            return await handler(event, data)

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

links = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="YouTube", url="https://www.youtube.com/channel/UCiikD7AdqsNEHQaoao1dzqQ"),
            InlineKeyboardButton(text="Telegram", url="tg://resolve?domain=oohta")
        ]
    ]
)

from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    KeyboardButtonPollType
)

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Смайлики"),
            KeyboardButton(text="Ссылки")
        ],
        [
            KeyboardButton(text="Калькулятор"),
            KeyboardButton(text="Спец. Кнопки")
        ],
    ],
    resize_keyboard=True, # клавиатура подстраивается под экран телефона
    one_time_keyboard=True, # клавиатура скрывается после первого использования
    input_field_placeholder="Выберете действие из меню",
    selective=True
)

links_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="YouTube", url="https://www.youtube.com/channel/UCiikD7AdqsNEHQaoao1dzqQ"),
            InlineKeyboardButton(text="Telegram", url="tg://resolve?domain=oohta")
        ]
    ]
)

spec_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Отправить ГЕО", request_location=True),
            KeyboardButton(text="Отправить Контакт", request_contact=True),
            KeyboardButton(text="Создать опрос", request_poll=KeyboardButtonPollType(type="regular")),
        ],
        [
            KeyboardButton(text="НАЗАД")
        ]
    ],
    resize_keyboard=True, # чтобы кнопки не были огромными
)


class Pagination(CallbackData, prefix="pag"):
    action: str
    page: int


def paginator(page: int = 0):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="🔙", callback_data=Pagination(action="prev", page=page).pack()),
        InlineKeyboardButton(text="▶", callback_data=Pagination(action="next", page=page).pack()),
        width=2
    )
    return builder.as_markup()


def calc_kb():
    items = [
        "1", "2", "3", "/",
        "4", "5", "6", "*",
        "7", "8", "9", "-",
        "0", ".", "=", "+",
    ]
    builder = ReplyKeyboardBuilder()
    [builder.button(text=item) for item in items]
    builder.button(text="НАЗАД")
    builder.adjust(4, 4, 4, 4, 1)
    return builder.as_markup(resize_keyboard=True)

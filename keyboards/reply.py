from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType, ReplyKeyboardRemove

main = ReplyKeyboardMarkup(
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

spec = ReplyKeyboardMarkup(
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


rmk = ReplyKeyboardRemove()

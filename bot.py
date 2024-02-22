import asyncio

from aiogram import Bot, Dispatcher

from callbacks import pagination
from config_reader import TOKEN
from handlers import bot_messages, user_commands, questionaire

from middlewares.check_sub import CheckSubscription


async def main():
    bot = Bot(TOKEN, parse_mode="HTML")
    dp = Dispatcher()

    dp.message.middleware(CheckSubscription())

    dp.include_routers(
        user_commands.router,
        pagination.router,
        questionaire.router,
        bot_messages.router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

import asyncio
from aiogram import Dispatcher, Bot
from aiogram.types import Message, KeyboardButton, InlineKeyboardButton, CallbackQuery
from config import token_bot
from handlers import messages


async def main():
    bot = Bot(token=token_bot)
    dp = Dispatcher()

    dp.include_routers(messages.router)

    #Пропускает все накопленные входящие мессейджи
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

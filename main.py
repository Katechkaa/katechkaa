import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")

dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: types.Message) -> None:
    """Обработчик команды /start."""
    user_name = message.from_user.full_name if message.from_user else "Пользователь"
    await message.answer(
        f"Привет, {user_name}! 👋\n"
        "Я бот-помощник для репетиторов и учеников.\n"
        "Здесь вы сможете вести расписание занятий и отслеживать оплаты."
    )


async def main() -> None:
    """Точка входа для запуска бота."""
    bot = Bot(token=BOT_TOKEN)
    logging.info("Запуск бота TutorReminder...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

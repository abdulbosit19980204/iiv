import asyncio
import logging
import sys
import wikipedia
from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

# Bot token can be obtained via https://t.me/BotFather
BOT_TOKEN="6741809709:AAFlnWrLVsdLEaa2DBvNy4AMZfenGddr3F8"
TOKEN = BOT_TOKEN  # Corrected line

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")
    print(message)
@dp.message()
async def dataSender(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
    except:
        await message.answer("Bunday shaxs topilmadi")

async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And run the events dispatching
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

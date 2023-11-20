import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold 
from config import BOT_TOKEN



dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    # await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")
    await message.answer(f'''
			Topilgan ma'lumotlar
			├FIO: {hbold(message.from_user.full_name)}
			├ID: {hbold(message.from_user.id)}
			├Username: @{hbold(message.from_user.username)}
            ├Premium : {hbold(message.from_user.is_premium)}
            ├Foydalanish tili : {hbold(message.from_user.language_code)}
			└Telefon nomer: {hbold(message.from_user.get_profile_photos())}
			''')
    

    
async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(BOT_TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
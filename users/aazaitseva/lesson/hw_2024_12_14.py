# import datetime
# from datetime import datetime
from datetime import datetime as dt

import pandas as pd

print(dt.now())

from aiogram import Bot, Dispatcher
from aiogram.types import Message
import asyncio
from aiogram.methods import DeleteWebhook


bot = Bot('7695535894:AAHJN0trkCMy2adp-du1jKeIO08ar-7oqmE')
dp = Dispatcher()

@dp.message()
async def cmd_start(message: Message, bot):
    if message.text in ['/start', 'start']:
        await bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}! Как дела?')
    else:
        await bot.send_message(message.chat.id, f'Круто! И у меня тоже')
        await bot.send_photo(
            chat_id=message.chat.id,
            photo='AgACAgIAAxkBAAMOZ12cIo2m1qwG8uMzb5YctHe57mIAAq_jMRsxN_BKuekc6zJy8bcBAAMCAAN4AAM2BA'
        )
        
# Запуск процесса поллинга новых апдейтов
async def main():
    # await bot(DeleteWebhook(drop_pending_updates=True))  # отключаем обновления
    await dp.start_polling(bot, skip_updates=True)
    
if __name__ == "__main__":
    asyncio.run(main())
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = " \n\n"
    text += "Biz faqat mp3,wav,wma,amr,ogg, ape,acc,spx,m4a,mp4 ko'rinishidagi malumotlarni qabul qilamiz. 🎧 \n"
    text += "15 MB gacha bo'lgan malumotlarni aniqlay olamiz. \n"
    text += "Siz yuborgan malumot sifati natijaga tasir ko'rsatishi mumkin. 🤕\n\n"
    
    await message.answer(text=text)
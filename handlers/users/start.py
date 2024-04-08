import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from keyboards.default.admin_info import menuAdmin
from loader import dp, db, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
    except sqlite3.IntegrityError as err:
        pass
    text = "<b> Assalamu alaykum </b>\n\n"
    text += f"Xush kelibsiz! {message.from_user.full_name}!\n\n\n"
    text += "<b>ARS Bot</b> sizga <i>Video</i> 🎞 va <i>Audio (mp3) 🎶</i> musiqalarini --Muallifi-- va --Musiqa nomini-- " \
            "aniqlab beradi.\n "
    text += "Bu bot orqali <i>Instagram</i> yoki shu kabi dasturlardan saqlangan  videolarni to'liq musiqasini " \
            "topishingiz mumkin \n\n\n "
    text += "p.s: Shunchaki musiqa nomi 🎶 va muallifi 🗣 aniqlanishi kerak bo'lgan <b>video</b> yoki <b>audio(mp3)</b> ni botga yuboring."
    await message.answer(text=text)
    # Adminga xabar beramiz
    count = db.count_users()[0]
    msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    await bot.send_message(chat_id=ADMINS[0], text=msg, reply_markup=menuAdmin)

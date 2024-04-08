import asyncio
import os
from pathlib import Path

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InputFile
from data.config import ADMINS
from keyboards.inline.test import test
from loader import dp, db, bot
from states.reklamaStates import ReklamaStates

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

downloads_path = Path().joinpath("reklama")
downloads_path.mkdir(parents=True, exist_ok=True)


@dp.message_handler(text="Barcha foydalanuvchilar", user_id=ADMINS)
async def get_all_users(message: types.Message):
    users = db.select_all_users()
    print(users[0][0])
    await message.answer(users)


@dp.message_handler(text="Reklama", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    # msg_admin = message.text
    # users = db.select_all_users()
    # for user in users:
    #     user_id = user[0]
    #     await bot.send_message(chat_id=user_id, text=msg_admin)
    #     await asyncio.sleep(0.05)
    msg = "Reklamani kiriting, reklama rasimlimi agar shunday bo'lsa '1' ni agar rasim bo'lmasa '2' ni kiriting."
    await message.answer(text=msg)
    await ReklamaStates.reklama.set()


@dp.message_handler(state=ReklamaStates.reklama)
async def get_all_users(message: types.Message, state: FSMContext):
    msg_admin = message.text
    if msg_admin == '1':
        await ReklamaStates.reklama1.set()
        msg = "Rasim kiritishingiz mumkin"
        await message.answer(text=msg)
    else:
        await ReklamaStates.reklama2.set()
        msg = "Iltimos matin kiriting."
        await message.answer(text=msg)

              # Bu rasimni saqlaydi
@dp.message_handler(state=ReklamaStates.reklama1, content_types='photo')
async def get_all_users(message: types.Message, state: FSMContext):
    msg_admin = await message.photo[-1].download(destination_dir=downloads_path)
    msg_text = "Siz yuborgan rasim qabul qilindi endi matin kiritishingiz mumkin, agar faqat rasimni yubormoqchi bo'lsangiz unda '1' raqamini kiriting"
    await message.answer(text=msg_text)
    await ReklamaStates.reklama3.set()


@dp.message_handler(state=ReklamaStates.reklama2)
async def get_all_users(message: types.Message, state: FSMContext):
    msg_admin = message.text
    users = db.select_all_users()
    for user in users:
        user_id = user[0]
        await bot.send_message(chat_id=user_id, text=msg_admin)
        await asyncio.sleep(0.05)
    await state.finish()
    msg = "Jarayon muvaffaqiyatli amalga oshirildi..."
    await message.answer(text=msg)


@dp.message_handler(state=ReklamaStates.reklama3)
async def get_all_users_rek(message: types.Message, state: FSMContext):
    msg_admin = message.text
    users = db.select_all_users()
    if msg_admin == '1':
        for user in users:
            for filename in os.listdir('reklama/photos/'):
                natija = filename
            img = f"reklama/photos/{natija}"
            rasim = InputFile(path_or_bytesio=img)
            user_id = user[0]
            await bot.send_photo(chat_id=user_id, photo=rasim)

            await asyncio.sleep(0.05)
            msg = "Jarayon muvaffaqiyatli amalga oshirildi..."
    else:
        for user in users:
            for filename in os.listdir('reklama/photos/'):
                natija = filename
            img = f"reklama/photos/{natija}"
            rasim = InputFile(path_or_bytesio=img)
            user_id = user[0]
            await bot.send_photo(chat_id=user_id, photo=rasim, caption=msg_admin)

            await asyncio.sleep(0.05)
            msg = "Jarayon mofaqiyatli amalga oshirildi..."

    # test = InlineKeyboardMarkup(
    #     inline_keyboard=[
    #         [
    #             InlineKeyboardButton(text='test', url='https://mohirdev.uz/courses/telegram/lesson/xabar-osti-tugmalari-inline-keyboards-1-qism/'),
    #         ]
    #     ]
    # )
    # # await message.answer(test)
    text_1 = "Link bormi"
    await message.answer(text=text_1)
    await message.answer(text=msg)
    await ReklamaStates.reklama4.set()
    # await state.finish()
    if os.path.isfile(img):
        os.remove(img)

@dp.message_handler(state=ReklamaStates.reklama4)
async def get_all_users(message: types.Message, state: FSMContext):
    msg_admin = message.text
    users = db.select_all_users()
    if msg_admin:
        for user in users:
            user_id = user[0]
            await bot.send_message(chat_id=user_id, text=msg_admin)
            await asyncio.sleep(0.05)
            text = msg_admin.split(",")
            text1 = text[0]
            text2 = text[1]
            test1 = f'https://t'
            test = InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(text=text1, url=test1),
                    ]
                ]
            )
            print(text1,text2)
            await message.answer(text='8', reply_markup=test)
    await state.finish()
    msg = "Jarayon muvaffaqiyatli amalga oshirildi..."
    await message.answer(text=msg)


@dp.message_handler(text="/cleandb", user_id=ADMINS)
async def get_all_users(message: types.Message):
    db.delete_users()
    await message.answer("Baza tozalandi!")


@dp.message_handler(text="Foydalanuvchilarning soni", user_id=ADMINS)
async def get_all_users(message: types.Message):
    count = db.count_users()[0]
    print(count)
    msg = f'Sizda {count} ta foydalanuvchi bor'
    await bot.send_message(chat_id=ADMINS[0], text=msg)

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuAdmin = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Barcha foydalanuvchilar '),
            KeyboardButton(text='Reklama'),
            KeyboardButton(text='Foydalanuvchilarning soni'),
        ],
    ],
    resize_keyboard=True
)

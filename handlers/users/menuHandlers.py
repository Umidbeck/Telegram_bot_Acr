from pathlib import Path

from aiogram.types import Message, InputFile, ReplyKeyboardRemove

from loader import dp, bot
from utils.acr_code import acr_cloud
from utils.you_tube_con import you_tube


@dp.message_handler(content_types='video')
@dp.message_handler(content_types='audio')
async def show_menu(message: Message):
    dow_name = message.from_user.id

    try:
        video_size = message.video.file_size
        size_file = video_size
    except:
        audio_size = message.audio.file_size
        size_file = audio_size
    if size_file <= 16000000:

        await message.answer(text="Malumot qabul qilindi...👨‍💻")
        downloads_path = Path().joinpath("downloads", f"{dow_name}")
        downloads_path.mkdir(parents=True, exist_ok=True)
        try:
            if await message.video.download(destination_dir=downloads_path):
                k = await message.video.download(destination_dir=downloads_path)
            else:
                k1 = await message.audio.download(destination_dir=downloads_path)
        except:
            k1 = await message.audio.download(destination_dir=downloads_path)

        link = await acr_cloud(dow_name)
        link_test = link
        if link is None:
            await message.answer(text="Afsuski musiqani aniqlanmadi...🤷‍♂️")
        else:
            text = link.split('+')
            text_music = "@ARS_IS_bot"
            text_music += '\n\n\n'
            text_music += f"Music author 🎤  ⏩  <i>{text[-1]}</i>\n"
            text_music += f"Music name 🎵  ⏩  <i>{text[0]}</i>\n\n"
            text_music += f"You Tube link: 👇👇👇\n"
            await message.answer(text=text_music)
            you_tube1 = await you_tube(link)
            await message.answer(you_tube1)
    else:
        await message.answer(text="Siz 15 MB gacha bo'lgan audio, video yubora olasiz")


@dp.message_handler(content_types='voice')
async def show_menu(message: Message):
    text = "Afsuski bunday malumotni qabul qila olmaymiz."
    await message.answer(text=text)


@dp.message_handler(content_types='any')
async def show_menu(message: Message):
    text = f"Siz faqat <b>Video</b> va <b>Audio (mp3)</b> yubora olasiz."
    await message.answer(text=text)

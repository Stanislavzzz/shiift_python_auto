from aiogram import types, Router
from aiogram.filters.command import Command

from utils.fox import fox
from utils.weather import get_weather
from keyboards.reply_keyboards import kb1, kb2
from keyboards.inline_keyboards import inline_keyboard


router = Router()


# /start
@router.message(Command('start'))
async def command_start(message: types.Message):
    print(message.text)
    print(message.chat.first_name)
    await message.answer(f"""Привет, {message.chat.first_name}!!!
Ты вызвал команду {message.text}""", reply_markup=kb1)


@router.message(Command('stop'))
async def command_stop(message: types.Message):
    await message.answer(f"""Пока, {message.chat.first_name}!!!
Ты вызвал команду {message.text}""", reply_markup=kb2)


@router.message(Command('ура'))
async def command_ura(message: types.Message):
    await message.answer(f"""Ура, я бот Shift""")


@router.message(Command('лиса'))
@router.message(Command('fox'))
async def command_fox(message: types.Message):
    image_fox = fox()
    await message.answer_photo(image_fox)


@router.message(Command('weather'))
async def command_fox(message: types.Message):
    temp = get_weather("Сочи")
    await message.answer(f"Погода в Сочи {temp}", reply_markup=inline_keyboard)

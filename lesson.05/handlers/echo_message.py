from aiogram import types, Router, F


router = Router()


@router.message(F.text)
async def command_weather(message: types.Message):
    if message.text == "/info":
        await message.answer(f"Что ты хочешь узнать?")
    else:
        await message.answer(f"Ты написал - {message.text}")

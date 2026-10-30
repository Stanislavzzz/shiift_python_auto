from aiogram import types, Router, F


router = Router()


@router.callback_query(F.data == "ask_chatgpt")
async def callback_ask_chatgpt(callback: types.CallbackQuery):
    await callback.message.answer('Ты нажал на кнопку GPT')
    await callback.answer()


@router.callback_query(F.data == "ask_yandex")
async def callback_ask_yandex(callback: types.CallbackQuery):
    await callback.message.answer('Ты нажал на кнопку Yandex')
    await callback.answer()
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


inline_button_1 = InlineKeyboardButton(text='Спросить у ChatGPT', callback_data='ask_chatgpt')
inline_button_2 = InlineKeyboardButton(text='Спросить у Yandex', callback_data='ask_yandex')


inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[[inline_button_1, inline_button_2]])
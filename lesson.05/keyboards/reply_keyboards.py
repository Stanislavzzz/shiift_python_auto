from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


button_1 = KeyboardButton(text='/start')
button_2 = KeyboardButton(text='/help')
button_3 = KeyboardButton(text='/stop')
button_4 = KeyboardButton(text='/info')
button_5 = KeyboardButton(text='/fox')
button_6 = KeyboardButton(text='Привет')
button_7 = KeyboardButton(text='Пока')


keyboard_1 = [
    [button_1, button_2, button_3],
    [button_4, button_5, button_6],
    [button_7],
]

keyboard_2 = [
    [button_1, button_3, button_5],
    [button_7, button_2]
]

kb1 = ReplyKeyboardMarkup(keyboard=keyboard_1, resize_keyboard=True)
kb2 = ReplyKeyboardMarkup(keyboard=keyboard_2, resize_keyboard=True)
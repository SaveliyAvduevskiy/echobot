from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_keyboard_1():
    keyboard = ReplyKeyboardMarkup(resize_keyboard= True)
    button_1 = KeyboardButton('ОТПРАВЬ ФОТО ТОКАРНОГО СТАНКА OPTIturn TU 2304')
    button_2 = KeyboardButton('УЙТИ К ДРУГОЙ КЛАВЕ(НЕ УХОДИ ПРОШУ ПРОШУ ПРОШУ🙏🙏🙏🙏')
    keyboard.add(button_1, button_2)
    return keyboard

def get_keyboard_2():
    keyboard_2 = ReplyKeyboardMarkup(resize_keyboard= True)
    button_3 = KeyboardButton('ОТПРАВЬ МНЕ ФОТО ИГОРЯ')
    button_4 = KeyboardButton('ВЕРНУТЬСЯ К ПРОШЛОЙ КЛАВЕ(УХОДИ ПРОШУ ПРОШУ ПРОШУ🙏🙏🙏🙏')
    keyboard_2.add(button_3, button_4)
    return keyboard_2
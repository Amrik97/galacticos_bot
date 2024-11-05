from telebot import types
from lang.kk import translations as kk
from lang.ru import translations as ru


user_languages = {}


def menu_buttons(lang_code):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

    #It'll choose texts depends on your chosen language
    language_pack = kk if lang_code == 'kk' else ru

    #Buttons for selecting, first step menu
    button_1 = types.KeyboardButton(language_pack['button_1'])
    button_2 = types.KeyboardButton(language_pack['button_2'])
    button_3 = types.KeyboardButton(language_pack['button_3'])
    button_4 = types.KeyboardButton(language_pack['button_4'])

    markup.add(button_1, button_2)
    markup.add(button_3, button_4)

    return markup
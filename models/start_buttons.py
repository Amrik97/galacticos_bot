import telebot
from telebot import types
import logging
from lang.kk import translations as kk
from lang.ru import translations as ru


user_languages = {}


def start_buttons(bot, message, lang_code):

    markup = types.InlineKeyboardMarkup()

    #buttons for choose language on nain page
    button_kk = types.InlineKeyboardButton(text='Қазақша', callback_data='lang_kk')
    button_ru = types.InlineKeyboardButton(text='Русский', callback_data='lang_ru')
    markup.add(button_kk, button_ru)


    welcome_message = (f"{kk['welcome']}\n\n{ru['welcome']}\n"
                       f"\n{kk['choose_language']}\n{ru['choose_language']}")

    bot.reply_to(message, welcome_message, reply_markup=markup)

    language_pack = kk if lang_code == 'kk' else ru

    #logging user click /start in telegram
    logging.info(f'User {message.from_user.username} ({message.from_user.id}) used /start')

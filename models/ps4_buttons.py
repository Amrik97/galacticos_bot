from telebot import types
from lang.kk import translations as kk
from lang.ru import translations as ru

user_languages = {}

def ps4_buttons(bot, message, lang_code):

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

    #It'll choose texts depends on your chosen language
    language_pack = kk if lang_code == 'kk' else ru

    # buttons for ps4 problems
    button_connecting_ps4 = types.KeyboardButton(language_pack['button_connecting_ps4'])
    button_game_blocked = types.KeyboardButton(language_pack['button_game_blocked'])
    button_game_blocked_password = types.KeyboardButton(language_pack['button_game_blocked_password'])
    button_download_games = types.KeyboardButton(language_pack['button_download_games'])
    button_no_works = types.KeyboardButton(language_pack['button_no_works'])
    restart_button = types.KeyboardButton(language_pack['restart_button'])
    ps4_gamepad = types.KeyboardButton(language_pack['ps4_gamepad'])

    markup.add(button_connecting_ps4, button_game_blocked)
    markup.add(restart_button, button_download_games)
    markup.add(button_no_works, ps4_gamepad)
    markup.add(button_game_blocked_password)


    return markup

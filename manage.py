import telebot
import logging
from telebot import types
from lang.kk import translations as kk
from lang.ru import translations as ru
from models.start_buttons import start_buttons
from models.ps4_buttons import ps4_buttons
from models.ps5_buttons import ps5_buttons
from menus.main_page import main_page
from menus.problem_page import problem_page, get_contact
from utils.one_time_request import one_time_request
from utils.redis_client_py import RedisClient  # Импортируем RedisClient
import time


redis_client = RedisClient()
#real job apir
bot = telebot.TeleBot('7867436867:AAHv72W1Rh2IMuc526hqCkLjsWpNW0doPgs')
#test
#bot = telebot.TeleBot('7090989975:AAF6jSPBpTwb4-hODXC3bo5bQaaRIj9Lmtw')

#real job id
channel_username = "-1002353491202"
#test
#channel_username = "-1002385224047"
channel_info = bot.get_chat(channel_username)

#if users do not want to text - only click button
user_languages = {}
# Словарь для хранения времени последнего запроса для каждого пользователя
last_contact_request = {}


logging.basicConfig(filename='bot_log.log', level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def get_language_pack(user_id):
    lang_code = user_languages.get(user_id, 'ru')  # По умолчанию русский
    return kk if lang_code == 'kk' else ru


def handle_response(user_id, chat_id, message_text_key, question_key):
    lang_code = user_languages.get(user_id)
    language_pack = kk if lang_code == 'kk' else ru
    bot.send_message(chat_id, language_pack[message_text_key])
    redis_client.record_user_click(user_id)

    if one_time_request(user_id):
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        button_yes = types.KeyboardButton(language_pack['yes'])
        button_no = types.KeyboardButton(language_pack['no'])
        markup.add(button_yes, button_no)
        bot.send_message(chat_id, language_pack[question_key], reply_markup=markup)
    else:
        bot.send_message(chat_id, language_pack['you_sent'])


def create_reply_markup(language_pack):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    button_yes = types.KeyboardButton(language_pack['yes'])
    button_no = types.KeyboardButton(language_pack['no'])
    markup.add(button_yes, button_no)
    return markup


#main page (choose language and welcome)
@bot.message_handler(commands=['start', 'Заново', 'Басынан'])
def handle_start(message):
    user_id = message.from_user.id
    start_buttons(bot, message, user_languages.get(user_id))


#Telling user which language he chose
@bot.callback_query_handler(func=lambda call: call.data.startswith('lang_'))
def callback_language_selection(call):
    user_id = call.from_user.id
    lang_code = 'kk' if call.data == 'lang_kk' else 'ru'
    user_languages[user_id] = lang_code
    language_pack = get_language_pack(user_id)

    redis_client.record_user_click(user_id)
    bot.send_message(call.message.chat.id, language_pack['greeting_message'])
    bot.send_message(call.message.chat.id, language_pack['help_user'], reply_markup=main_page(lang_code))


#after choosing ps4 problems
@bot.message_handler(func=lambda message: message.text == get_language_pack(message.from_user.id).get('button_1'))
def first_page(message):
    user_id = message.from_user.id
    markup = ps4_buttons(bot, message, user_languages.get(user_id))
    redis_client.record_user_click(user_id)
    language_pack = get_language_pack(user_id)
    bot.reply_to(message, language_pack['problem_message'], reply_markup=markup)


#after choosing Подключение PS4
@bot.message_handler(func=lambda message: message.text == get_language_pack(message.from_user.id).get('button_connecting_ps4'))
def answer_1(message):
    handle_response(message.from_user.id, message.chat.id, 'answer_1', 'question_1')


@bot.message_handler(func=lambda message: message.text == get_language_pack(message.from_user.id).get('button_2'))
def second_page(message):
    user_id = message.from_user.id
    markup = ps5_buttons(bot, message, user_languages.get(user_id))
    redis_client.record_user_click(user_id)
    language_pack = get_language_pack(user_id)
    bot.reply_to(message, language_pack['problem_message'], reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == get_language_pack(message.from_user.id).get('button_connecting_ps5'))
def answer_11(message):
    handle_response(message.from_user.id, message.chat.id, 'answer_10', 'question_1')


@bot.message_handler(func=lambda message: message.text == get_language_pack(message.from_user.id).get('button_game_blocked'))
def answer_2(message):
    handle_response(message.from_user.id, message.chat.id, 'answer_2', 'question_1')


@bot.message_handler(func=lambda message: message.text == get_language_pack(message.from_user.id).get('button_game_blocked_password_ps5'))
def answer_13(message):
    handle_response(message.from_user.id, message.chat.id, 'answer_13', 'question_1')


@bot.message_handler(func=lambda message: message.text == get_language_pack(message.from_user.id).get('button_game_blocked_ps5'))
def answer_12(message):
    handle_response(message.from_user.id, message.chat.id, 'answer_12', 'question_1')


@bot.message_handler(func=lambda message: message.text == get_language_pack(message.from_user.id).get('button_game_blocked_password'))
def answer_3(message):
    handle_response(message.from_user.id, message.chat.id, 'answer_3', 'question_1')


@bot.message_handler(func=lambda message: message.text == get_language_pack(message.from_user.id).get('button_download_games'))
def answer_4(message):
    handle_response(message.from_user.id, message.chat.id, 'answer_4', 'question_1')


@bot.message_handler(func=lambda message: message.text == get_language_pack(message.from_user.id).get('button_download_games_p5'))
def answer_14(message):
    handle_response(message.from_user.id, message.chat.id, 'answer_14', 'question_1')


@bot.message_handler(func=lambda message: message.text == get_language_pack(message.from_user.id).get('button_no_works'))
def answer_5(message):
    user_id = message.from_user.id
    lang_code = user_languages.get(user_id)  # Получаем язык пользователя
    language_pack = kk if lang_code == 'kk' else ru  # Определяем язык
    text = language_pack['answer_5']
    redis_client.record_user_click(user_id)
    bot.send_message(message.chat.id, text)


@bot.message_handler(func=lambda message: message.text == get_language_pack(message.from_user.id).get('ps4_gamepad'))
def answer_9(message):
    handle_response(message.from_user.id, message.chat.id, 'answer_9', 'question_1')


@bot.message_handler(func=lambda message: message.text == get_language_pack(message.from_user.id).get('ps5_gamepad'))
def answer_11(message):
    handle_response(message.from_user.id, message.chat.id, 'answer_11', 'question_1')


@bot.message_handler(func=lambda message: message.text == get_language_pack(message.from_user.id).get('button_3'))
def answer_6(message):
    handle_response(message.from_user.id, message.chat.id, 'answer_6', 'question_1')


@bot.message_handler(func=lambda message: message.text == get_language_pack(message.from_user.id).get('button_4'))
def answer_8(message):
    handle_response(message.from_user.id, message.chat.id, 'answer_8', 'question_1')


# Обработчик "Да" или "Нет"
@bot.message_handler(func=lambda message: message.text in ['/Да', '/Нет', '/Иә', '/Жоқ'])
def response_handler(message):
    user_id = message.from_user.id
    lang_code = user_languages.get(user_id, 'ru')
    redis_client.record_user_click(user_id)
    problem_page(lang_code, message, bot)


# Обработчик получения контакта
@bot.message_handler(content_types=['contact'])
def get_contact_handler(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    lang_code = user_languages.get(user_id, 'ru')
    language_pack = kk if lang_code == 'kk' else ru

    # Получаем сохранённую жалобу пользователя
    selected_complaint = redis_client.get_value(f"user:{user_id}:complaint")

    if not selected_complaint:
        bot.send_message(chat_id, language_pack['unrecognized_command'])
        return  # Прерываем обработку, если жалоба отсутствует

    # Получаем время последнего запроса контакта
    last_contact_time = redis_client.get_last_contact_time(user_id)

    if last_contact_time is None or time.time() - last_contact_time > 86400:
        # Разрешаем запрос контакта и сохраняем время
        redis_client.set_last_contact_time(user_id)
        redis_client.record_user_click(user_id)
        get_contact(message, lang_code, bot, selected_complaint)  # Теперь передаём selected_complaint
    else:
        # Отправляем сообщение, что контакт уже был запрашиваем ранее
        bot.send_message(chat_id, language_pack['you_sent'])


while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        logging.error(f"Ошибка: {e}. Перезапуск через 5 секунд...")
        time.sleep(5)

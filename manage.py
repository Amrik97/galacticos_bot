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


bot = telebot.TeleBot('7378047405:AAF2aqD8eXNZRjn1Uem7chAoJolT-taPuj0')


channel_username = "-1002353491202"
channel_info = bot.get_chat(channel_username)

#if users do not want to text - only click button
user_languages = {}

# Словарь для хранения времени последнего запроса для каждого пользователя
last_contact_request = {}



logging.basicConfig(filename='bot_log.log', level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


#main page (choose language and welcome)
@bot.message_handler(commands=['start', 'Заново', 'Басынан'])
def handle_start(message):
    user_id = message.from_user.id
    lang_code = user_languages.get(user_id)
    redis_client.record_user_click(user_id)
    start_buttons(bot, message, lang_code)


#Telling user which language he chose
@bot.callback_query_handler(func=lambda call: call.data.startswith('lang_'))
def callback_language_selection(call):
    user_id = call.from_user.id
    lang_code = 'kk' if call.data == 'lang_kk' else 'ru'
    user_languages[user_id] = lang_code
    language_pack = kk if lang_code == 'kk' else ru

    redis_client.record_user_click(user_id)

    bot.send_message(call.message.chat.id, language_pack['greeting_message'])

    bot.send_message(call.message.chat.id, language_pack['help_user'], reply_markup=main_page(lang_code))


#after choosing ps4 problems
@bot.message_handler(func=lambda message: message.text in ['Проблемы с PS4', 'PS4-пен проблема бар'])
def first_page(message):
    user_id = message.from_user.id
    lang_code = user_languages.get(user_id)
    markup = ps4_buttons(bot, message, lang_code)
    redis_client.record_user_click(user_id)

    if lang_code == 'kk':
        language_pack = kk
    else:
        language_pack = ru
    problem_message = language_pack['problem_message']
    bot.reply_to(message, problem_message, reply_markup=markup)

#after choosing Подключение PS4
@bot.message_handler(func=lambda message: message.text in ['Подключение PS4', 'PS4 қосу'])
def answer_1(message):
    user_id = message.from_user.id
    lang_code = user_languages.get(user_id)  # Получаем язык пользователя
    language_pack = kk if lang_code == 'kk' else ru  # Определяем язык
    text = language_pack['answer_1']
    bot.send_message(message.chat.id, text)

    redis_client.record_user_click(user_id)


    if one_time_request(user_id):
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        button_yes = types.KeyboardButton(language_pack['yes'])
        button_no = types.KeyboardButton(language_pack['no'])
        markup.add(button_yes, button_no)
        bot.send_message(message.chat.id, language_pack['question_1'], reply_markup=markup)
    else:
        bot.send_message(message.chat.id, language_pack['you_sent'])

@bot.message_handler(func=lambda message: message.text in ['Проблемы с PS5', 'PS5-пен проблема бар'])
def second_page(message):
    user_id = message.from_user.id
    lang_code = user_languages.get(user_id)
    markup = ps5_buttons(bot, message, lang_code)
    redis_client.record_user_click(user_id)

    if lang_code == 'kk':
        language_pack = kk
    else:
        language_pack = ru
    problem_message = language_pack['problem_message']
    bot.reply_to(message, problem_message, reply_markup=markup)


@bot.message_handler(func=lambda message: message.text in ['Подключение PS5', 'PS5 қосу'])
def answer_11(message):
    user_id = message.from_user.id
    lang_code = user_languages.get(user_id)  # Получаем язык пользователя
    language_pack = kk if lang_code == 'kk' else ru  # Определяем язык
    text = language_pack['answer_10']
    bot.send_message(message.chat.id, text)
    redis_client.record_user_click(user_id)


    if one_time_request(user_id):
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        button_yes = types.KeyboardButton(language_pack['yes'])
        button_no = types.KeyboardButton(language_pack['no'])
        markup.add(button_yes, button_no)
        bot.send_message(message.chat.id, language_pack['question_1'], reply_markup=markup)
    else:
        bot.send_message(message.chat.id, language_pack['you_sent'])




@bot.message_handler(func=lambda message: message.text in ['На играх PS4 появился замочек и они не запускаются', 'Ps4 ойындарында құлып белгісі пайда болды, және олар ашылмай жатыр'])
def answer_2(message):
    user_id = message.from_user.id
    lang_code = user_languages.get(user_id)  # Получаем язык пользователя
    language_pack = kk if lang_code == 'kk' else ru  # Определяем язык
    text = language_pack['answer_2']
    bot.send_message(message.chat.id, text)

    redis_client.record_user_click(user_id)


    if one_time_request(user_id):
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        button_yes = types.KeyboardButton(language_pack['yes'])
        button_no = types.KeyboardButton(language_pack['no'])
        markup.add(button_yes, button_no)
        bot.send_message(message.chat.id, language_pack['question_1'], reply_markup=markup)
    else:
        bot.send_message(message.chat.id, language_pack['you_sent'])

@bot.message_handler(func=lambda message: message.text in ['На Ps5 играх появился замочек, а при запуске игры система просит ввести пароль', 'Ps5 ойындарында құлып белгісі пайда болды, ал ойынды іске қосқанда жүйе пароль енгізуді сұрайды'])
def answer_13(message):
    user_id = message.from_user.id
    lang_code = user_languages.get(user_id)  # Получаем язык пользователя
    language_pack = kk if lang_code == 'kk' else ru  # Определяем язык
    text = language_pack['answer_13']
    bot.send_message(message.chat.id, text)

    redis_client.record_user_click(user_id)

    if one_time_request(user_id):
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        button_yes = types.KeyboardButton(language_pack['yes'])
        button_no = types.KeyboardButton(language_pack['no'])
        markup.add(button_yes, button_no)
        bot.send_message(message.chat.id, language_pack['question_1'], reply_markup=markup)
    else:
        bot.send_message(message.chat.id, language_pack['you_sent'])

@bot.message_handler(func=lambda message: message.text in ['На играх PS5 появился замочек и они не запускаются', 'Ps5 ойындарында құлып белгісі пайда болды, және олар ашылмай жатыр'])
def answer_12(message):
    user_id = message.from_user.id
    lang_code = user_languages.get(user_id)  # Получаем язык пользователя
    language_pack = kk if lang_code == 'kk' else ru  # Определяем язык
    text = language_pack['answer_12']
    bot.send_message(message.chat.id, text)

    redis_client.record_user_click(user_id)


    if one_time_request(user_id):
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        button_yes = types.KeyboardButton(language_pack['yes'])
        button_no = types.KeyboardButton(language_pack['no'])
        markup.add(button_yes, button_no)
        bot.send_message(message.chat.id, language_pack['question_1'], reply_markup=markup)
    else:
        bot.send_message(message.chat.id, language_pack['you_sent'])


@bot.message_handler(func=lambda message: message.text in ['На Ps4 играх появился замочек, а при запуске игры система просит ввести пароль', 'Ps4 ойындарында құлып белгісі пайда болды, ал ойынды іске қосқанда жүйе пароль енгізуді сұрайды'])
def answer_3(message):
    user_id = message.from_user.id
    lang_code = user_languages.get(user_id)  # Получаем язык пользователя
    language_pack = kk if lang_code == 'kk' else ru  # Определяем язык
    text = language_pack['answer_3']
    bot.send_message(message.chat.id, text)

    redis_client.record_user_click(user_id)

    if one_time_request(user_id):
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        button_yes = types.KeyboardButton(language_pack['yes'])
        button_no = types.KeyboardButton(language_pack['no'])
        markup.add(button_yes, button_no)
        bot.send_message(message.chat.id, language_pack['question_1'], reply_markup=markup)
    else:
        bot.send_message(message.chat.id, language_pack['you_sent'])


@bot.message_handler(func=lambda message: message.text in ['Как загрузить игры с интернета на ps4?', 'Ps4-ке ғаламтордан ойындарды қалай жүктеуге болады?'])
def answer_4(message):
    user_id = message.from_user.id
    lang_code = user_languages.get(user_id)  # Получаем язык пользователя
    language_pack = kk if lang_code == 'kk' else ru  # Определяем язык
    text = language_pack['answer_4']
    bot.send_message(message.chat.id, text)

    redis_client.record_user_click(user_id)

    if one_time_request(user_id):
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        button_yes = types.KeyboardButton(language_pack['yes'])
        button_no = types.KeyboardButton(language_pack['no'])
        markup.add(button_yes, button_no)
        bot.send_message(message.chat.id, language_pack['question_1'], reply_markup=markup)
    else:
        bot.send_message(message.chat.id, language_pack['you_sent'])


@bot.message_handler(func=lambda message: message.text in ['Как загрузить игры с интернета на ps5?', 'Ps5-ке ғаламтордан ойындарды қалай жүктеуге болады?'])
def answer_14(message):
    user_id = message.from_user.id
    lang_code = user_languages.get(user_id)  # Получаем язык пользователя
    language_pack = kk if lang_code == 'kk' else ru  # Определяем язык
    text = language_pack['answer_14']
    bot.send_message(message.chat.id, text)

    redis_client.record_user_click(user_id)

    if one_time_request(user_id):
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        button_yes = types.KeyboardButton(language_pack['yes'])
        button_no = types.KeyboardButton(language_pack['no'])
        markup.add(button_yes, button_no)
        bot.send_message(message.chat.id, language_pack['question_1'], reply_markup=markup)
    else:
        bot.send_message(message.chat.id, language_pack['you_sent'])



@bot.message_handler(func=lambda message: message.text in ['Что-то не работает?', 'Бірдеме жұмыс жасамай тұрма?'])
def answer_5(message):
    user_id = message.from_user.id
    lang_code = user_languages.get(user_id)  # Получаем язык пользователя
    language_pack = kk if lang_code == 'kk' else ru  # Определяем язык
    text = language_pack['answer_5']
    redis_client.record_user_click(user_id)
    bot.send_message(message.chat.id, text)


@bot.message_handler(func=lambda message: message.text in ['Как подключить второй джойстик на пс4', 'PS4-ке екінші джойстык қалай қосуға болады?'])
def answer_9(message):
    user_id = message.from_user.id
    lang_code = user_languages.get(user_id)  # Получаем язык пользователя
    language_pack = kk if lang_code == 'kk' else ru  # Определяем язык
    text = language_pack['answer_9']
    bot.send_message(message.chat.id, text)
    redis_client.record_user_click(user_id)

    redis_client.record_user_click(user_id)

    if one_time_request(user_id):
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        button_yes = types.KeyboardButton(language_pack['yes'])
        button_no = types.KeyboardButton(language_pack['no'])
        markup.add(button_yes, button_no)
        bot.send_message(message.chat.id, language_pack['question_1'], reply_markup=markup)
    else:
        bot.send_message(message.chat.id, language_pack['you_sent'])


@bot.message_handler(func=lambda message: message.text in ['Как подключить второй джойстик на пс5', 'PS5-ке екінші джойстык қалай қосуға болады?'])
def answer_11(message):
    user_id = message.from_user.id
    lang_code = user_languages.get(user_id)  # Получаем язык пользователя
    language_pack = kk if lang_code == 'kk' else ru  # Определяем язык
    text = language_pack['answer_11']
    bot.send_message(message.chat.id, text)
    redis_client.record_user_click(user_id)

    redis_client.record_user_click(user_id)

    if one_time_request(user_id):
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        button_yes = types.KeyboardButton(language_pack['yes'])
        button_no = types.KeyboardButton(language_pack['no'])
        markup.add(button_yes, button_no)
        bot.send_message(message.chat.id, language_pack['question_1'], reply_markup=markup)
    else:
        bot.send_message(message.chat.id, language_pack['you_sent'])


@bot.message_handler(func=lambda message: message.text in ['Вопросы доставки', 'Жеткізу бойынша сұрақтар'])
def answer_6(message):
    user_id = message.from_user.id
    lang_code = user_languages.get(user_id)  # Получаем язык пользователя
    language_pack = kk if lang_code == 'kk' else ru  # Определяем язык
    text = language_pack['answer_6']
    bot.send_message(message.chat.id, text)

    redis_client.record_user_click(user_id)

    if one_time_request(user_id):
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        button_yes = types.KeyboardButton(language_pack['yes'])
        button_no = types.KeyboardButton(language_pack['no'])
        markup.add(button_yes, button_no)
        bot.send_message(message.chat.id, language_pack['question_1'], reply_markup=markup)
    else:
        bot.send_message(message.chat.id, language_pack['you_sent'])


@bot.message_handler(func=lambda message: message.text in ['Нужен цифровой код с почты', 'Поштадан цифрлық код керек'])
def answer_8(message):
    user_id = message.from_user.id
    lang_code = user_languages.get(user_id)  # Получаем язык пользователя
    language_pack = kk if lang_code == 'kk' else ru  # Определяем язык
    text = language_pack['answer_8']
    bot.send_message(message.chat.id, text)

    redis_client.record_user_click(user_id)

    if one_time_request(user_id):
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        button_yes = types.KeyboardButton(language_pack['yes'])
        button_no = types.KeyboardButton(language_pack['no'])
        markup.add(button_yes, button_no)
        bot.send_message(message.chat.id, language_pack['question_1'], reply_markup=markup)
    else:
        bot.send_message(message.chat.id, language_pack['you_sent'])



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
    lang_code = user_languages.get(user_id, 'ru')
    redis_client.record_user_click(user_id)
    get_contact(lang_code, message, bot)

while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Ошибка: {e}. Перезапуск через 5 секунд...")
        time.sleep(5)

from telebot import types
from lang.kk import translations as kk
from lang.ru import translations as ru
from utils.redis_client_py import RedisClient


redis_client = RedisClient()

user_languages = {}


def problem_page(lang_code, message, bot):
    user_id = message.from_user.id
    language_pack = kk if lang_code == 'kk' else ru
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    # Добавляем кнопки с жалобами
    complaint_types = [
        language_pack['button_connecting_ps4'],
        language_pack['button_game_blocked'],
        language_pack['button_game_blocked_password'],
        language_pack['button_game_blocked_password_ps5'],
        language_pack['button_download_games'],
        language_pack['button_no_works'],
        language_pack['ps4_gamepad'],
        language_pack['button_connecting_ps5'],
        language_pack['ps5_gamepad'],
        language_pack['button_3'],
        language_pack['button_4'],
    ]

    for complaint in complaint_types:
        markup.add(complaint)
    if message.text == language_pack['yes']:
        # Прощаемся с пользователем и завершаем сессию
        bot.send_message(message.chat.id, language_pack['bye'])
        redis_client.set_value(f"user:{user_id}:decision", "finished")  # Устанавливаем статус завершения
        return  # Завершаем обработку

    bot.send_message(message.chat.id, language_pack['choose_complaint'], reply_markup=markup)
    bot.register_next_step_handler(message, handle_complaint_selection, lang_code, bot, markup)


def handle_complaint_selection(message, lang_code, bot, markup):
    user_id = message.from_user.id
    language_pack = kk if lang_code == 'kk' else ru

    # Проверяем, выбрал ли пользователь "Да"

    # Создаем словарь для сопоставления текстов жалоб с внутренними значениями
    complaint_mapping = {
        language_pack['button_connecting_ps4']: "Подключение PS4",
        language_pack['button_game_blocked']: "Игра заблокирована",
        language_pack['button_game_blocked_password']: "Заблокированная игра по паролю Ps4",
        language_pack['button_game_blocked_password_ps5']: "Заблокированная игра по паролю Ps5",
        language_pack['button_download_games']: "Загрузка игр",
        language_pack['button_no_works']: "Ничего не работает",
        language_pack['ps4_gamepad']: "Геймпад PS4",
        language_pack['button_connecting_ps5']: "Подключение PS5",
        language_pack['ps5_gamepad']: "Геймпад PS5",
        language_pack['button_3']:"Вопросы по доставке",
        language_pack['button_4']:"Нужен цифровой код с почты",
    }

    # Получаем выбранную жалобу из сообщения
    selected_complaint = complaint_mapping.get(message.text)

    if selected_complaint:
        contact_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        share_contact_btn = types.KeyboardButton(language_pack['share_contact'], request_contact=True)
        contact_markup.add(share_contact_btn)

        redis_client.set_value(f"user:{user_id}:complaint", selected_complaint)
        redis_client.set_value(f"user:{user_id}:decision", "waiting")

        bot.send_message(message.chat.id, language_pack['send_you_number'], reply_markup=contact_markup)
        bot.register_next_step_handler(message, get_contact, lang_code, bot, selected_complaint)
    else:
        bot.send_message(message.chat.id, language_pack['unrecognized_command'], reply_markup=markup)


def get_contact(message, lang_code, bot, selected_complaint):
    user_id = message.from_user.id
    language_pack = kk if lang_code == 'kk' else ru

    decision = redis_client.get_value(f"user:{user_id}:decision")

    if message.contact and decision == "waiting":
        contact_text = message.contact.phone_number
        redis_client.set_value(f"user:{user_id}:contact", contact_text)

        bot.send_message(
            message.chat.id,
            language_pack['call_time_confirm'],  # Или другое сообщение
            reply_markup=types.ReplyKeyboardRemove()
        )

        # Prompt the user to choose a convenient call-back time
        # time_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        # time_options = [language_pack['time_1'], language_pack['time_2'], language_pack['time_3'],
        #                 language_pack['time_4'], language_pack['time_5']]
        # for option in time_options:
        #     time_markup.add(option)

        # bot.send_message(message.chat.id, language_pack['choose_call_time'],) reply_markup=time_markup)
        bot.register_next_step_handler(message, lang_code, bot, selected_complaint)

    elif decision == "sent":
        bot.send_message(message.chat.id, language_pack['you_sent'], reply_markup=types.ReplyKeyboardRemove())
    else:
        bot.send_message(message.chat.id, language_pack['no_contact_received'],
                         reply_markup=types.ReplyKeyboardRemove())


# def get_call_time(message, lang_code, bot, selected_complaint):
#     user_id = message.from_user.id
#     language_pack = kk if lang_code == 'kk' else ru
#
#     # Retrieve and store the selected time in Redis
#     selected_time = message.text
#     redis_client.set_value(f"user:{user_id}:call_time", selected_time)
#
    # Confirm with the user and send the final message
    # bot.send_message(
    #     message.chat.id,
    #     language_pack['call_time_confirm'].format(time=selected_time),
    #     reply_markup=types.ReplyKeyboardRemove()
    # )

    # Send the complete complaint message to the channel
    channel_username = "-1002385224047"
    complaint_message = (
        f"Пользователь @{message.from_user.username} отправил контакт: {redis_client.get_value(f'user:{user_id}:contact')}. "
        f"Проблема: {selected_complaint}. "
        # f"Удобное время для звонка: {selected_time}."
    )

    # Update the decision status
    redis_client.set_value(f"user:{user_id}:decision", "sent")

    bot.send_message(channel_username, complaint_message, reply_markup=types.ReplyKeyboardRemove())

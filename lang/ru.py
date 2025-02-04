from lang.colors import Colors
from colorama import init, Fore, Style

init()


translations = {
    'hello': 'Здравствуйте',
    'welcome': 'Доброго времени суток, дорогой покупатель!'
               '\nЯ чат-бот – Ваша техническая поддержка по вопросам Playstation',
    'greeting_morning': 'Доброе утро!',
    'greeting_day': 'Доброго времени суток!',
    'greeting_evening': 'Добрый вечер!',
    'main_menu_greeting': 'Привет!',


    'problem_message': 'Какие сложности возникли?',
    'contact_request': 'Пожалуйста, отправьте свой контакт для завершения покупки.',
    'purchase_confirmation': 'Ваш запрос на покупку отправлен. Мы скоро свяжемся с вами!',
    'help_user': 'Чем я могу Вам помочь?',
    'questions_p4': 'Подскажите, какая проблема возникла?',
    'choose_language': 'Выберите язык:',
    'greeting_message': 'Вы выбрали русский язык!',

#
    'back_button': '/Назад',
    'restart_button': 'Заново',
    'button_1': 'Проблемы с PS4',
    'button_2': 'Проблемы с PS5',
    'button_3': 'Вопросы доставки',
    'button_4': 'Нужен цифровой код с почты',

# buttons for ps4 problems
    'button_connecting_ps4': 'Подключение PS4',
    'button_connecting_ps5': 'Подключение PS5',
    'button_game_blocked': 'На играх PS4 появился замочек и они не запускаются',
    'button_game_blocked_ps5': 'На играх PS5 появился замочек и они не запускаются',
    'button_game_blocked_password': 'На Ps4 играх появился замочек, а при запуске игры система просит ввести пароль',
    'button_game_blocked_password_ps5': 'На Ps5 играх появился замочек, а при запуске игры система просит ввести пароль',
    'button_download_games': 'Как загрузить игры с интернета на ps4?',
    'button_download_games_p5': 'Как загрузить игры с интернета на ps5?',
    'button_no_works': 'Что-то не работает?',
    'ps4_gamepad': 'Как подключить второй джойстик на пс4',
    'ps5_gamepad': 'Как подключить второй джойстик на пс5',
    'question_1': 'Вам удалось решить Вашу проблему?',


# connecting problem's answers
    'answer_1':  'Первое подключение пс4.'
                '\n\nТекстовая инструкция и видео инструкция (Ссылка на видео: https://www.youtube.com/watch?v=e-tdz7fxq7M&ab_channel=Galacticos-%D0%B2%D1%81%D1%91%D0%BF%D1%80%D0%BEPlayStation)'
                '\n\nПодключите кабель HDMI к разъему HDMI OUT на задней панели консоли PS4®.\nЗатем подключи этот же кабель HDMI к разъему HDMI твоего телевизора. '
                '\n\nПодключите кабель питания к разъему AC IN на задней панели консоли PS4. '
                '\n\nНадежно вставьте сетевую вилку в розетку электросети. '
                '\n\nНа пульте от телевизора найдите кнопку переключения между разъемами и выбери HDMI. '
                '\n\nПодключите кабель USB к передней части панели пс4 '
                '\n\nПодключите второй конец шнура USB – microUSB к джойстику и нажми кнопку ПС в центре джойстика. '
                '\n\nЗаходим в любой User',
    'answer_2': 'Текстовая инструкция и видео инструкция (Ссылка на YouTube: https://www.youtube.com/watch?v=dzvtbPdc3CM&ab_channel=Galacticos-%D0%B2%D1%81%D1%91%D0%BF%D1%80%D0%BEPlayStation) '
                '\n\nЗаходим в аккаунт с играми по секретному коду L2R2L1R1 (кнопки расположены на джойстике) '
                '\n\nНастройки —> Управление учетной записью \nАктивировать, как основную систему PS —> Активировать —> Ок \nВосстановить лицензии —> Восстановить —> Ок '
                '\n\nПосле активации и успешной разблокировки игр, желательно перейти в Сеть и убрать '
                'галочку «подключение к интернету» (это делается во избежание в '
                'дальнейшем деактивации игр и проверки лицензий от Sony). Далее обязательно заходим в'
                ' \n\nПитание —> Выйти из системы PS и сменяем пользователя на любой User. '
                'Запускаем игру и наслаждаемся процессом.',
    'answer_3': 'Текстовая инструкция и видео инструкция (Ссылка на YouTube: https://www.youtube.com/watch?v=3ackK2hF-Xc&ab_channel=Galacticos-%D0%B2%D1%81%D1%91%D0%BF%D1%80%D0%BEPlayStation)'
                '\n\nНастройки —> Управление учетной записью —> Войти в Сеть.'
                '\n\nЛогин уже будет у вас отображаться, а пароль от аккаунта ты сможешь найти на последней странице гарантийного талона(обычно он начинается fipa7578ХХХХ). Введите пароль и нажми кнопку Войти в сеть'
                '\n\nАктивировать, как основную систему PS —> Активировать —> Ок'
                '\n\nВосстановить лицензии —> Восстановить —> Ок'
                '\n\nПосле активации и успешной разблокировки игр, желательно перейти в Сеть и убрать галочку '
                '«подключение к интернету» (это делается во избежание в дальнейшем деактивации игр и проверки '
                'лицензий от Sony).'
                '\n\nДалее обязательно заходим в Питание —> Выйти из системы PS и сменяем '
                'пользователя на любой User. Запускаем игру и наслаждаемся процессом.',
    'answer_4': 'Текстовая инструкция и видео инструкция (Cсылка на YouTube: https://www.youtube.com/watch?v=QTW-RPKUHL4&ab_channel=Galacticos-%D0%B2%D1%81%D1%91%D0%BF%D1%80%D0%BEPlayStation)'
                '\n\nЗаходим в любой User —> Настройки —> Сеть —> Установить соединение с интернетом '
                '(для быстрого скачивания игр рекомендуем подключить Lan кабель).'
                '\n\nПереходим в главное меню, в правом левом углу находим раздел Уведомления, где заходим в Загрузки, '
                'вы увидите сколько займет времени скачивание игр (Внимание в некоторых случаях игры могут быть уже'
                ' скачены и готовы, в таком случае вы можете запустить игру).'
                '\n\nПосле подключения к интернету, при необходимости догрузки игр, в главном меню заходим в Питание,'
                ' выбираем пункт Перейти в режим покоя (В режиме покоя скачивание продолжается).',
    'answer_5': 'Что-то не работает? \n\n- джойстик \n\n- Приставка \n\nНапишите нам на ватсап на номер '
                       'тех поддержки: 87472223521 '
                       '\n\nЗВОНКИ НЕ ПРИНИМАЮТСЯ. ТОЛЬКО ВАТСАП!!! '
                       '\n\nГрафик работы: с понедельника по пятницу С 9:00 – до 18:00',
    'answer_6': '3.1 Доставка по Казахстану: '
                '\n\nЕсли у вас возникли вопросы по доставке в разные города Казахстана, вам необходимо позвонить по номеру 9999, продиктовать ваш номер заказа и задать свой вопрос менеджеру Каспий банка. '
                '\n\n3.2 Доставка по Алмате. '
                '\n\nНаш магазин находится в городе Алматы. Если у вас возникли вопросы по времени доставки позвоните на номер: 87476595882',
    'answer_8': 'Если у вас запрашивает код, после ввода пароля от аккаунта, '
               'наш менеджер с вами свяжется и отправит вам код. \n\nПожалуйста ожидайте и ничего не трогайте',
    'answer_9': 'Как подключить второй джойстик на пс4 (Ссылка на YouTube: https://www.youtube.com/watch?v=FPZXzE-lfw0&ab_channel=Galacticos-%D0%B2%D1%81%D1%91%D0%BF%D1%80%D0%BEPlayStation)'
                '\n\nПодключите первый джойстик по кабелю USB и зайдите в аккаунт USER1.'
                '\n\nОтключите джойстик от кабеля и подключи второй джойстик по кабелю.'
                '\n\nНажмите кнопку пс в центре джойстика и выбери аккаунт USER2.'
                '\n\nВы подключили 2 джойстика. Но работать одновременно они будут только в играх, предназначенных для двоих и более игроков.',
    'answer_10': 'Текстовая инструкция и видео инструкция (Ссылка на YouTube: https://www.youtube.com/watch?v=vzAq2Bi8cLM&ab_channel=Galacticos-%D0%B2%D1%81%D1%91%D0%BF%D1%80%D0%BEPlayStation)'
                '\n\nПодключи кабель HDMI к разъему HDMI OUT на задней панели консоли PS5®.\nЗатем подключи этот же кабель HDMI к разъему HDMI твоего телевизора. '
                '\n\nПодключи кабель питания к разъему AC IN на задней панели консоли PS5. '
                '\n\nНадежно вставь сетевую вилку в розетку электросети. '
                '\n\nНа пульте от телевизора найдите кнопку переключения между разъемами и выбери HDMI. '
                '\n\nПодключи кабель USB к передней части панели PS5 '
                '\n\nПодключи второй конец шнура USB – microUSB к джойстику и нажми кнопку ПС в центре джойстика. '
                '\n\nЗаходим в любой User',
    'answer_11': 'Как подключить второй джойстик на пс5 (Ссылка на YouTube: https://www.youtube.com/watch?v=FPZXzE-lfw0&ab_channel=Galacticos-%D0%B2%D1%81%D1%91%D0%BF%D1%80%D0%BEPlayStation)'
                '\n\nПодключите первый джойстик по кабелю USB и зайдите в аккаунт USER1.'
                '\n\nОтключите джойстик от кабеля и подключи второй джойстик по кабелю.'
                '\n\nНажмите кнопку пс в центре джойстика и выбери аккаунт USER2.'
                '\n\nВы подключили 2 джойстика. Но работать одновременно они будут только в играх, предназначенных для двоих и более игроков.',
    'answer_12': 'Текстовая инструкция и видео инструкция (Ссылка на YouTube: https://www.youtube.com/watch?v=LgGLWeX5a6c&ab_channel=Galacticos-%D0%B2%D1%81%D1%91%D0%BF%D1%80%D0%BEPlayStation)'
                '\n\nНастройки —> Управление учетной записью —> Войти в Сеть.'
                '\n\nЛогин уже будет у вас отображаться, а пароль от аккаунта ты сможешь найти на последней странице гарантийного талона(обычно он начинается fipa7578ХХХХ). Введите пароль и нажми кнопку Войти в сеть'
                '\n\nАктивировать, как основную систему PS —> Активировать —> Ок'
                '\n\nВосстановить лицензии —> Восстановить —> Ок'
                '\n\nПосле активации и успешной разблокировки игр, желательно перейти в Сеть и убрать галочку '
                '«подключение к интернету» (это делается во избежание в дальнейшем деактивации игр и проверки '
                'лицензий от Sony).'
                '\n\nДалее обязательно заходим в Питание —> Выйти из системы PS и сменяем '
                'пользователя на любой User. Запускаем игру и наслаждаемся процессом.',
    'answer_13': 'Текстовая инструкция и видео инструкция (Ссылка на YouTube: https://www.youtube.com/watch?v=cPTvOlj2riM&ab_channel=Galacticos-%D0%B2%D1%81%D1%91%D0%BF%D1%80%D0%BEPlayStation)'
                '\n\nНастройки —> Управление учетной записью —> Войти в Сеть.'
                '\n\nЛогин уже будет у вас отображаться, а пароль от аккаунта ты сможешь найти на последней странице гарантийного талона(обычно он начинается fipa7578ХХХХ). Введите пароль и нажми кнопку Войти в сеть'
                '\n\nАктивировать, как основную систему PS —> Активировать —> Ок'
                '\n\nВосстановить лицензии —> Восстановить —> Ок'
                '\n\nПосле активации и успешной разблокировки игр, желательно перейти в Сеть и убрать галочку '
                '«подключение к интернету» (это делается во избежание в дальнейшем деактивации игр и проверки '
                'лицензий от Sony).'
                '\n\nДалее обязательно заходим в Питание —> Выйти из системы PS и сменяем '
                'пользователя на любой User. Запускаем игру и наслаждаемся процессом.',
    'answer_14': 'Текстовая инструкция и видео инструкция (Cсылка на YouTube: https://www.youtube.com/watch?v=xn9PCwJe5Kc&ab_channel=Galacticos-%D0%B2%D1%81%D1%91%D0%BF%D1%80%D0%BEPlayStation)'
                 '\n\nЗаходим в любой User —> Настройки —> Сеть —> Установить соединение с интернетом '
                 '(для быстрого скачивания игр рекомендуем подключить Lan кабель).'
                 '\n\nПереходим в главное меню, в правом левом углу находим раздел Уведомления, где заходим в Загрузки, '
                 'вы увидите сколько займет времени скачивание игр (Внимание в некоторых случаях игры могут быть уже'
                 ' скачены и готовы, в таком случае вы можете запустить игру).'
                 '\n\nПосле подключения к интернету, при необходимости догрузки игр, в главном меню заходим в Питание,'
                 ' выбираем пункт Перейти в режим покоя (В режиме покоя скачивание продолжается).',
    # we ask did you finish your problem?
    'yes': '/Да',
    'no': '/Нет',
    'bye': 'Рад был помочь! Приятного пользования. Если возникнут дополнительные вопросы – обращайтесь',
    'we_call_you': 'Очень жаль. Не расстраивайтесь, с вами свяжется менеджер в рабочее время, чтобы помочь.'
                   ' Запрос уже отправлен',
    'asks_again': 'Ваш запрос в обработке. Пожалуйста ожидайте. Менеджер отвечает в порядке очередности',
    'so_sad':'Очень жаль. Не расстраивайтесь, с вами свяжется менеджер в рабочее время, чтобы помочь. Запрос уже отправлен.',
    'send_you_number': 'Пожалуйста, отправьте свой контактный номер.',
    'you_welcome': 'Рад был помочь! Приятного пользования. Если возникнут дополнительные вопросы – обращайтесь',
    'you_sent': 'У вас есть отправленный в обработку запрос. Пожалуйста ожидайте. Менеджер отвечает в порядке очередности',
    'share_contact': 'Поделиться контактом',
    'no_contact_received': 'no_contact_received',
    'unrecognized_command': 'unrecognized_command',

    'choose_complaint': 'Выберите проблему',
    'time_1': 'С 9:00 до 11:00',
    'time_2': 'С 11:00 до 13:00',
    'time_3': 'С 13:00 до 15:00',
    'time_4': 'С 15:00 до 17:00',
    'time_5': 'С 17:00 до 18:00',
    'choose_call_time': 'Пожалуйста, выберите удобное время для звонка: ',
    'call_time_confirm': 'С вами свяжется менеджер в рабочее время, чтобы помочь.',
                   # ' Запрос уже отправлен. Вы выбрали: {time} для звонка',
}
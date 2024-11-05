from datetime import datetime, timedelta

# Словарь для хранения времени последнего запроса для каждого пользователя
last_contact_request = {}


def one_time_request(user_id):
    """
    Проверяет, может ли пользователь отправить контактные данные.
    Если прошло менее 24 часов с момента последней отправки контакта, возвращает False.
    Иначе обновляет время последнего запроса и возвращает True.

    Parameters:
    user_id (int): Идентификатор пользователя в Telegram.

    Returns:
    bool: True, если можно запросить контакт; False в противном случае.
    """
    if user_id in last_contact_request:
        last_request_time = last_contact_request[user_id]
        if datetime.now() - last_request_time < timedelta(days=1):
            return False
    last_contact_request[user_id] = datetime.now()
    return True

from datetime import datetime, timedelta

last_button_clicks = {}


def last_clicked_button(user_id, button_id):
    current_time = datetime.now()

    # Сохраняем время последнего клика и ID кнопки
    last_button_clicks[user_id] = (current_time, button_id)
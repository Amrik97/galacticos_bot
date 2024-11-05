import redis

class RedisClient:
    def __init__(self, host='localhost', port=6379, db=0):
        self.client = redis.StrictRedis(host=host, port=port, db=db, decode_responses=True)

    def set_value(self, key, value):
        """Устанавливает значение по ключу в Redis."""
        self.client.set(key, value)

    def get_value(self, key):
        """Получает значение по ключу из Redis."""
        return self.client.get(key)

    def record_user_click(self, user_id):
        """Пример метода для записи клика пользователя."""
        self.client.incr(f"user:{user_id}:clicks")
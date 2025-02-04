import redis
import time

class RedisClient:
    def __init__(self, host='localhost', port=6379, db=0):
        self.client = redis.StrictRedis(host=host, port=port, db=db, decode_responses=True)

    def set_value(self, key, value):
        self.client.set(key, value)

    def get_value(self, key):
        return self.client.get(key)

    def record_user_click(self, user_id):
        self.client.incr(f"user:{user_id}:clicks")

    def get_last_contact_time(self, user_id):
        last_time = self.client.get(f"user:{user_id}:last_contact_time")
        return float(last_time) if last_time else None

    def set_last_contact_time(self, user_id):
        self.client.set(f"user:{user_id}:last_contact_time", time.time())

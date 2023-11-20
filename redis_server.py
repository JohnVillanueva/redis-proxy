import redis
import os

from dotenv import load_dotenv
load_dotenv()


class RedisServer:

    conn: redis.Redis

    def __init__(self, host=os.getenv('HOST'), port=os.getenv('PORT'), max_conns=os.getenv('MAX_CONNECTIONS')):

        self.host = host
        self.port = port
        self.conn = redis.Redis(host=host, port=port, max_connections=max_conns, decode_responses=True)

    def Set(self, key: str, value):

        result = self.conn.set(key, value)

        return result

    def Get(self, key: str):

        value = self.conn.get(key)

        return value

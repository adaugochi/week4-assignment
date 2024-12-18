import os
import redis
from flask import Flask

app = Flask(__name__)

# Connect to Redis
redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = int(os.getenv('REDIS_PORT', 6379))
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)


@app.route('/')
def home():
    redis_client.incr('counter')
    counter = redis_client.get('counter')
    return f"Hello, Docker! You've visited this page {counter} times."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

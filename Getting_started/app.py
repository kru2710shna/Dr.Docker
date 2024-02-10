from flask import Flask
import os
import time 
import redis
# The open-source, in-memory data store used by millions 
# of developers as a cache, vector database, document 
# database, streaming engine, and message broker

app = Flask(__name__)
cache = redis.Redis(host = 'redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            cache.reset_retry_count()
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exec:
            if redis ==0:
                raise exec
            retries -= 1
            time.sleep(0.5)
            
@app.route('/', methods=['GET'])
def home():
    count = get_hit_count()
    return "Hello Krushna! I have been seen {} times\n".format(count)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=8000)
    


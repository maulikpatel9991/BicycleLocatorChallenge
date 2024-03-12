import random
import sys
import uuid

import redis
import pandas as pd

# Connect to Redis database
redis_db = redis.StrictRedis(host='redis-15165.c301.ap-south-1-1.ec2.cloud.redislabs.com',
                             port=15165,
                             db=0,
                             password='YtXbZmArFC8Yd4pshzNpUhGGFLXeU6y2',
                             decode_responses=True)


def load_bicycle_data(number):
    for i in range(0, int(number)):
        bicycle_id = str(uuid.uuid4())
        print(bicycle_id)
        latitude = 20
        longitude = 20
        redis_db.set(bicycle_id, f"{latitude},{longitude}")


load_bicycle_data(sys.argv[1])
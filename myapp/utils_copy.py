import random
import sys
import uuid

import redis
import pandas as pd



def load_bicycle_data(number: int)-> dict:
    """
    Data add in redis server
    """
    # Connect to Redis database
    redis_db = redis.StrictRedis(host='redis-15165.c301.ap-south-1-1.ec2.cloud.redislabs.com',
                                 port=15165,
                                 db=0,
                                 password='YtXbZmArFC8Yd4pshzNpUhGGFLXeU6y2',
                                 decode_responses=True)

    for i in range(0, 10):
        bicycle_id = str(uuid.uuid4())
        latitude = 20
        longitude = 20
        redis_db.set(bicycle_id, f"{latitude},{longitude}")

# Call function to load bicycle data
load_bicycle_data(10)
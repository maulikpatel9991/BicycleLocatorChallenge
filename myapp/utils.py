import redis
import pandas as pd


def load_bicycle_data(parquet_file):
    redis_db = redis.StrictRedis(host='redis-15165.c301.ap-south-1-1.ec2.cloud.redislabs.com',
                                 port=15165,
                                 db=0,
                                 password='YtXbZmArFC8Yd4pshzNpUhGGFLXeU6y2',
                                 decode_responses=True)
    df = pd.read_parquet(parquet_file)

    bicycle_data = {}
    print("done")
    for index, row in df.iterrows():
        bicycle_id = row['BicycleID']
        latitude = row['Latitude']
        longitude = row['Longitude']
        bicycle_data[bicycle_id] = f"{latitude},{longitude}"

    redis_db.mset(bicycle_data)

load_bicycle_data('bicycle_data.parquet')
# http://127.0.0.1:8000/locate_bicycle/?latitude=67&longitude=45
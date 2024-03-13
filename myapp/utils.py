import redis
import pandas as pd


def load_bicycle_data(parquet_file: str) -> dict:
    """
    Data add in Redis Server
    """

    # Connect to Redis database
    redis_db = redis.StrictRedis(host='redis-15165.c301.ap-south-1-1.ec2.cloud.redislabs.com',
                                 port=15165,
                                 db=0,
                                 password='YtXbZmArFC8Yd4pshzNpUhGGFLXeU6y2',
                                 decode_responses=True)
    # Load data from Parquet file
    df = pd.read_parquet(parquet_file)
    # empty dictionary to store bicycle data
    bicycle_data = {}
    for index, row in df.iterrows():
        # bicycle ID, latitude, and longitude
        bicycle_id = row['BicycleID']
        latitude = row['Latitude']
        longitude = row['Longitude']
        # Store latitude and longitude as a string in the format "latitude,longitude"
        bicycle_data[bicycle_id] = f"{latitude},{longitude}"

    redis_db.mset(bicycle_data)

# Call function to load bicycle data
load_bicycle_data('bicycle_data.parquet')

# http://127.0.0.1:8000/locate_bicycle/?latitude=67&longitude=45
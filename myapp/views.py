from django.http import JsonResponse
from django.views.decorators.http import require_GET
import redis
import geopy.distance
import json
from django.http import JsonResponse
from flask import Flask, request, jsonify
from myapp.utils import load_bicycle_data

# Connect to Redis database
redis_db = redis.StrictRedis(host='redis-15165.c301.ap-south-1-1.ec2.cloud.redislabs.com',
                             port=15165,
                             db=0,
                             password='YtXbZmArFC8Yd4pshzNpUhGGFLXeU6y2',
                             decode_responses=True)

# Call function to load bicycle data
load_bicycle_data('bicycle_data.parquet')

@require_GET
def locate_bicycle(request) -> json:
    """
    Get data for redis server
    """
    # get latitude and longitude from request parameters
    latitude = float(request.GET.get('latitude'))
    longitude = float(request.GET.get('longitude'))
    try:
        # Check if latitude is within the valid range [-90, 90]
        if not (-90 <= latitude <= 90):
            raise ValueError("Latitude must be in the [-90; 90] range.")
    except ValueError as e:
        # Handle the ValueError exception
        return JsonResponse({'error': str(e)})

    min_distance = float('inf')
    nearest_bicycles = []                           # list nearest_bicycles
    all_keys = redis_db.keys('*')                   # Retrieve all keys from Redis database

    pipeline = redis_db.pipeline()
    for key in all_keys:
        pipeline.get(key)
    results = pipeline.execute()

    # Process the results
    for key, value in zip(all_keys, results):
        bicycle_id = key
        bicycle_location = value

        # Split location string into latitude and longitude
        bike_lat, bike_lon = map(float, bicycle_location.split(','))
        distance = geopy.distance.geodesic((latitude, longitude), (bike_lat, bike_lon)).meters
        # Check if the distance is smaller than current minimum distance
        if distance < min_distance:
            # If yes, update minimum distance and nearest bicycles list
            min_distance = distance
            nearest_bicycles = [{'BicycleID': key, 'Latitude': bike_lat, 'Longitude': bike_lon, "Name": "Maulik"}]
        elif distance == min_distance:
            # If distance is equal to minimum distance, add bicycle to nearest bicycles list
            nearest_bicycles.append({'BicycleID': key, 'Latitude': bike_lat, 'Longitude': bike_lon, "Name": "Maulik"})

    # If nearest bicycles found, return them as JSON response
    if nearest_bicycles:
        return JsonResponse({'bicycles': nearest_bicycles})
    else:
        # If no bicycles found, return error message as JSON response
        return JsonResponse({'error': 'No bicycles Data found'})

@require_GET
def bicycle_locator_data(request) -> json:
    nearest_bicycles = []                           # list nearest_bicycles

    all_keys = redis_db.keys('*')                   # Retrieve all keys from Redis database

    pipeline = redis_db.pipeline()
    for key in all_keys:
        pipeline.get(key)
    results = pipeline.execute()

    for key, value in zip(all_keys, results):
        bicycle_id = key
        bicycle_location = value
        bike_lat, bike_lon = map(float, bicycle_location.split(','))

        # append data from nearest bicycles list
        nearest_bicycles.append(
            {'BicycleID': bicycle_id, 'Latitude': bike_lat, 'Longitude': bike_lon, "Name": "Maulik"})

    # return json data
    return JsonResponse({'bicycles': nearest_bicycles})

# https://syaamex.hashnode.dev/devops-project-jenkins-cicd#heading-step-0-creating-andamp-connecting-an-ec2-instance
from django.http import JsonResponse
from django.views.decorators.http import require_GET
import redis
import geopy.distance
import json
from django.http import JsonResponse
from myapp.utils import load_bicycle_data

# Connect to Redis database
redis_db = redis.StrictRedis(host='redis-15165.c301.ap-south-1-1.ec2.cloud.redislabs.com',
                             port=15165,
                             db=0,
                             password='YtXbZmArFC8Yd4pshzNpUhGGFLXeU6y2',
                             decode_responses=True)

load_bicycle_data('bicycle_data.parquet')

@require_GET
def locate_bicycle(request):
    latitude = float(request.GET.get('latitude'))
    longitude = float(request.GET.get('longitude'))

    nearest_bicycles = []  # Store all nearest bicycles
    min_distance = float('inf')

    for key in redis_db.scan_iter("*"):
        print("demo")
        bicycle_location = redis_db.get(key)
        bike_lat, bike_lon = map(float, bicycle_location.split(','))
        distance = geopy.distance.geodesic((latitude, longitude), (bike_lat, bike_lon)).meters
        if distance < min_distance:
            min_distance = distance
            nearest_bicycles = [{'BicycleID': key, 'Latitude': bike_lat, 'Longitude': bike_lon, "Name": "Maulik"}]
        elif distance == min_distance:
            nearest_bicycles.append({'BicycleID': key, 'Latitude': bike_lat, 'Longitude': bike_lon, "Name": "Maulik"})

    if nearest_bicycles:
        return JsonResponse({'bicycles': nearest_bicycles})
    else:
        return JsonResponse({'error': 'No bicycles found'})
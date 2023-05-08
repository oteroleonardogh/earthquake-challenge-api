from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from geopy.distance import distance
from geopy.point import Point

from datetime import datetime

from ..models.city_model import City
from ..services.earthquake_service import get_earthquake_data

def get_earthquakes(request, start_time, end_time, min_magnitude, order_by='-time'):
    query_url = request.build_absolute_uri()
    data = get_earthquake_data(start_time, end_time, min_magnitude, order_by, query_url)

    response_data = {
        'metadata': data['metadata'],
        'earthquakes': data['features'],
        'bbox': data['bbox']
    }

    return JsonResponse(response_data)

def nearest_earthquake_to_city(request, city, start_time, end_time, min_magnitude):

    city_obj = get_object_or_404(City, name=city)
    query_url = request.build_absolute_uri()
    earthquake_data = get_earthquake_data(start_time, end_time, min_magnitude, 'time', query_url)

    # Find the closest earthquake
    closest_earthquake = None
    closest_distance = float('inf')
    for earthquake in earthquake_data['features']:
        coords = earthquake['geometry']['coordinates']
        earthquake_point = Point(coords[1], coords[0])
        city_point = Point(city_obj.latitude, city_obj.longitude)
        dist = distance(earthquake_point, city_point).km
        if dist < closest_distance:
            closest_distance = dist
            closest_earthquake = earthquake

    if closest_earthquake:
        mag = closest_earthquake['properties']['mag']
        place = closest_earthquake['properties']['place']
        time = closest_earthquake['properties']['time']
        time_str = datetime.fromtimestamp(time / 1000).strftime('%Y-%m-%d %H:%M:%S')
        message = f'The closest earthquake to {city} was a M {mag} - {place} on {time_str}'
    else:
        message = f'No earthquakes found near {city}'

    response = {'message': message}
    return JsonResponse(response)
import os
import requests
import json
from ..models import EarthquakeQuery
from config.cache_config import cache

USGS_API_URL = os.getenv(
    'USGS_API_URL', 
    'https://earthquake.usgs.gov/fdsnws/event/1/query.geojson'
)

def get_earthquake_data(start_time, end_time, min_magnitude, order_by, query_url):
    # Fetch the data from the USGS API or cache
    data = fetch_earthquake_data(start_time, end_time, min_magnitude, order_by)
    # Save the data to the database only if it's not present in the cache
    if data['from_cache'] == False:
        save_earthquake_data(data, query_url, start_time, end_time, min_magnitude, order_by)

    return data

def fetch_earthquake_data(start_time, end_time, min_magnitude, order_by):

    cache_key = f"earthquake_data:{start_time}:{end_time}:{min_magnitude}:{order_by}"
    print('cache_key: ', cache_key) # TODO: improve this to use a better logging system
    data = cache.get(cache_key)
    if data is not None:
        print('Using data retrived from cache.')
        
        return json.loads(data)  # Remove the unnecessary decode() call

    params = {
        'starttime': start_time,
        'endtime': end_time,
        'minmagnitude': min_magnitude,
        'orderby': order_by
    }
    print('Calling USGS API.')
    response = requests.get(USGS_API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        data['from_cache'] = False
        cache.set(cache_key, json.dumps(data), 24*3600)  # Cache for 1 day
        return data
    else:
        raise Exception(f"Error fetching data from USGS API: {response.status_code}")

def save_earthquake_data(data, query_url, start_time, end_time, min_magnitude, order_by):
    earthquake_query = EarthquakeQuery.objects.create(
        query_url=query_url,
        start_time=start_time,
        end_time=end_time,
        min_magnitude=min_magnitude,
        order_by=order_by,
        type=data['type'],
        metadata=data['metadata'],
        bbox=data['bbox'],
        features=data['features'],
    )
    earthquake_query.save()
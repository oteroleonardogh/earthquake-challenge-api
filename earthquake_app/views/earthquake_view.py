from django.http import JsonResponse
from ..services.earthquake_service import get_earthquake_data

def get_earthquakes(request, start_time, end_time, min_magnitude, order_by):
    query_url = request.build_absolute_uri()
    data = get_earthquake_data(start_time, end_time, min_magnitude, order_by, query_url)

    response_data = {
        'metadata': data['metadata'],
        'earthquakes': data['features'],
        'bbox': data['bbox']
    }

    return JsonResponse(response_data)

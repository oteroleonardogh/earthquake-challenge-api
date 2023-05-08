from django.urls import path, re_path
from .views import CityView, get_earthquakes, nearest_earthquake_to_city

urlpatterns = [
    path('cities/', CityView.as_view(), name='city_view'),
    path('earthquake_data/<str:start_time>/<str:end_time>/<str:min_magnitude>/<str:order_by>/', get_earthquakes, name='get_earthquakes'),
    # re_path(r'^nearest_earthquake/(?P<city>[\w\s,]+)/'
    #     r'(?P<start_time>\d{4}-\d{2}-\d{2})/'
    #     r'(?P<end_time>\d{4}-\d{2}-\d{2})/'
    #     r'(?P<min_magnitude>\d+\.\d+)/$',
    #     nearest_earthquake_to_city, name='nearest_earthquake'),
    path('nearest_earthquake/<str:city>/<str:start_time>/<str:end_time>/<str:min_magnitude>/', nearest_earthquake_to_city, name='nearest_earthquake_to_city')
]

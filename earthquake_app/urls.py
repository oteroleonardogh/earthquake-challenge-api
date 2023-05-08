from django.urls import path
from .views import CityView, get_earthquakes

urlpatterns = [
    path('earthquake_data/<str:start_time>/<str:end_time>/<str:min_magnitude>/<str:order_by>/', get_earthquakes, name='get_earthquakes'),
    path('cities/', CityView.as_view(), name='city_view'),
]

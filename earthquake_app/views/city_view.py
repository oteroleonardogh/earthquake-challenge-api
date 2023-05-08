from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from ..services.city_service import create_city

class CityView(APIView):

    def post(self, request, *args, **kwargs):
        name = request.data.get('name')
        latitude = request.data.get('latitude')
        longitude = request.data.get('longitude')
        population = request.data.get('population')

        if not all([name, latitude, longitude, population]):
            return JsonResponse({"error": "Missing required fields"}, status=status.HTTP_400_BAD_REQUEST)

        city = create_city(name, latitude, longitude, population)
        return JsonResponse({"message": "City created successfully", "city_id": city.id}, status=status.HTTP_201_CREATED)

    # def get(self, request, *args, **kwargs):
        # Implement the logic for GET method here

    # def put(self, request, *args, **kwargs):
        # Implement the logic for PUT method here

    # def delete(self, request, *args, **kwargs):
        # Implement the logic for DELETE method here
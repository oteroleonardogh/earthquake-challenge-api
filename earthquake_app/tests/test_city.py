from django.test import TestCase
from unittest.mock import patch, MagicMock
from earthquake_app.services.city_service import create_city


class TestCreateCity(TestCase):
    @patch('earthquake_app.services.city_service.City')
    def test_create_city(self, mock_city):
        # arrange
        name = "Test City"
        latitude = 0.12345
        longitude = 0.54321
        population = 1000

        mock_city.return_value = MagicMock()

        # act
        create_city(name, latitude, longitude, population)

        # assert
        mock_city.assert_called_once_with(name=name, latitude=latitude, longitude=longitude, population=population)
        mock_city.return_value.save.assert_called_once()

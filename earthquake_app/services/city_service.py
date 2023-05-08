from ..models import City

def create_city(name, latitude, longitude, population):
    city = City(
        name=name,
        latitude=latitude,
        longitude=longitude,
        population=population
    )
    city.save()
    return city

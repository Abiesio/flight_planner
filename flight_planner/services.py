import os

from flight_planner.persistence import InMemoryStore, FileStore, SQLStore


# Четене на променливата на околната среда DATA_STORE
store_type = os.environ.get('DATA_STORE', 'inmemory')
# Избор на подходящото хранилище
if store_type == 'inmemory':
    store = InMemoryStore()
elif store_type == 'file':
    store = FileStore()
elif store_type == 'sql':
    store = SQLStore()
else:
    raise ValueError(f"Unsupported store type: {store_type}")

# Create the appropriate store

class CityService:
    """ A bunch of @staticmethod's """

    @staticmethod
    def create_city(name: str):
        """ Създаване на нов град """
        city = {'name': name}
        store.add_city(city)
        return city

    @staticmethod
    def get_all_cities():
        """ Връща всички градове """
        return store.get_all_cities()

    @staticmethod
    def get_city_by_id(city_id: int):
        """ Връща град по ID """
        return store.get_city_by_id(city_id)

    @staticmethod
    def delete_city_by_id(city_id: int):
        """ Изтриване на град по ID """
        store.delete_city_by_id(city_id)

    @staticmethod
    def delete_all_cities():
        """ Изтриване на всички градове """
        store.delete_all_cities()
    
class AirportService:
    """ A bunch of @staticmethod's """

    @staticmethod
    def create_airport(name: str, city_id: int):
        """ Създаване на ново летище """
        airport = {'name': name, 'city_id': city_id}
        store.add_airport(airport)
        return airport

    @staticmethod
    def get_all_airports():
        """ Връща всички летища """
        return store.get_all_airports()

    @staticmethod
    def get_airport_by_id(airport_id: int):
        """ Връща летище по ID """
        return store.get_airport_by_id(airport_id)

    @staticmethod
    def delete_airport_by_id(airport_id: int):
        """ Изтриване на летище по ID """
        store.delete_airport_by_id(airport_id)

    @staticmethod
    def delete_all_airports():
        """ Изтриване на всички летища """
        store.delete_all_airports()

class FlightService:
    """ A bunch of @staticmethod's """


    @staticmethod
    def create_flight(departure_airport, arrival_airport, departure_time, travel_time, price):
        """ Създаване на нов полет """
        flight = {
            'departure_airport': departure_airport,
            'arrival_airport': arrival_airport,
            'departure_time': departure_time,
            'travel_time': travel_time,
            'price': price
        }
        store.add_flight(flight)
        return flight

    @staticmethod
    def get_all_flights():
        """ Връща всички полети """
        return store.get_all_flights()

    @staticmethod
    def get_flight_by_id(flight_id: int):
        """ Връща полет по ID """
        return store.get_flight_by_id(flight_id)

    @staticmethod
    def delete_flight_by_id(flight_id: int):
        """ Изтриване на полет по ID """
        store.delete_flight_by_id(flight_id)

    @staticmethod
    def delete_all_flights():
        """ Изтриване на всички полети """
        store.delete_all_flights()

    @staticmethod
    def search_flights(departure_city, arrival_city, min_price, max_price, min_departure_time, max_departure_time):
        """ Търсене на полети по зададени критерии """
        return store.search_flights(departure_city, arrival_city, min_price, max_price, min_departure_time, max_departure_time)
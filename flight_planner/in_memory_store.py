class InMemoryStore:
    def __init__(self):
        # Списъци за съхраняване на градове, летища и полети
        self.cities = []
        self.airports = []
        self.flights = []

    # Методи за управление на градовете
    def add_city(self, city):
        self.cities.append(city)

    def get_all_cities(self):
        return self.cities

    def get_city_by_id(self, city_id):
        return next((city for city in self.cities if city['id'] == city_id), None)

    def delete_city_by_id(self, city_id):
        self.cities = [city for city in self.cities if city['id'] != city_id]

    def delete_all_cities(self):
        self.cities = []

    # Методи за управление на летищата
    def add_airport(self, airport):
        self.airports.append(airport)

    def get_all_airports(self):
        return self.airports

    def get_airport_by_id(self, airport_id):
        return next((airport for airport in self.airports if airport['id'] == airport_id), None)

    def delete_airport_by_id(self, airport_id):
        self.airports = [airport for airport in self.airports if airport['id'] != airport_id]

    def delete_all_airports(self):
        self.airports = []

    # Методи за управление на полетите
    def add_flight(self, flight):
        self.flights.append(flight)

    def get_all_flights(self):
        return self.flights

    def get_flight_by_id(self, flight_id):
        return next((flight for flight in self.flights if flight['id'] == flight_id), None)

    def delete_flight_by_id(self, flight_id):
        self.flights = [flight for flight in self.flights if flight['id'] != flight_id]

    def delete_all_flights(self):
        self.flights = []
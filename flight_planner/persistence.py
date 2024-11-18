import json
import sqlite3

class InMemoryStore:
    """ In-Memory storage for data persistence """
    
    def __init__(self):
        self.cities = {}
        self.airports = {}
        self.flights = {}
    
    # Пример за метод за добавяне на град
    def add_city(self, city_id, city_data):
        self.cities[city_id] = city_data
    
    def get_city(self, city_id):
        return self.cities.get(city_id, None)
    
    def get_all_cities(self):
        return list(self.cities.values())
    
    def delete_city(self, city_id):
        if city_id in self.cities:
            del self.cities[city_id]

# Това е пример за клас за файлово съхранение
class FileStore:
    """ File storage for data persistence (using JSON) """
    
    def __init__(self, file_name='data.json'):
        self.file_name = file_name
        self.load_data()

    def load_data(self):
        """ Зареждаме данни от JSON файл """
        try:
            with open(self.file_name, 'r') as f:
                data = json.load(f)
                self.cities = data.get("cities", {})
                self.airports = data.get("airports", {})
                self.flights = data.get("flights", {})
        except FileNotFoundError:
            self.cities = {}
            self.airports = {}
            self.flights = {}

    def save_data(self):
        """ Записваме данни във файл """
        with open(self.file_name, 'w') as f:
            json.dump({
                "cities": self.cities,
                "airports": self.airports,
                "flights": self.flights
            }, f)
    
    def add_city(self, city_id, city_data):
        self.cities[city_id] = city_data
        self.save_data()
    
    def get_city(self, city_id):
        return self.cities.get(city_id, None)
    
    def get_all_cities(self):
        return list(self.cities.values())

    def delete_city(self, city_id):
        if city_id in self.cities:
            del self.cities[city_id]
            self.save_data()

# Това е пример за клас за SQL база данни
class SQLStore:
    """ SQL storage for data persistence (using SQLite) """
    
    def __init__(self, db_name='flight_planner.db'):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self):
        """ Създаваме таблиците ако не съществуват """
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS cities (id INTEGER PRIMARY KEY, name TEXT)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS airports (id INTEGER PRIMARY KEY, name TEXT, city_id INTEGER)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS flights (id INTEGER PRIMARY KEY, departure_airport INTEGER, arrival_airport INTEGER, departure_time TEXT, travel_time INTEGER, price TEXT)''')
        self.conn.commit()

    def add_city(self, city_id, city_data):
        """ Добавяме нов град """
        self.cursor.execute('INSERT INTO cities (id, name) VALUES (?, ?)', (city_id, city_data))
        self.conn.commit()
    
    def get_city(self, city_id):
        """ Връщаме град по ID """
        self.cursor.execute('SELECT * FROM cities WHERE id=?', (city_id,))
        return self.cursor.fetchone()
    
    def get_all_cities(self):
        """ Връщаме всички градове """
        self.cursor.execute('SELECT * FROM cities')
        return self.cursor.fetchall()
    
    def delete_city(self, city_id):
        """ Изтриваме град по ID """
        self.cursor.execute('DELETE FROM cities WHERE id=?', (city_id,))
        self.conn.commit()

    def close(self):
        """ Затваряме връзката към базата данни """
        self.conn.close()